import requests

def fetch_earthquake_data(api_key: str):
    """
    從氣象局 API 取得最新地震資料。
    """
    api = (
        f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/"
        f"E-A0015-001?Authorization={api_key}&limit=1&format=JSON&AreaName="
    )
    response = requests.get(api, headers={'Accept': 'application/json'})
    return response.json()


def summarize_earthquake_info(data):
    earthquake = data['records']['Earthquake'][0]
    info = earthquake['EarthquakeInfo']
    intensity = earthquake['Intensity']

    # 提取基本地震資訊
    disaster_name = earthquake['ReportContent']
    epicenter = info['Epicenter']['Location']
    magnitude = info['EarthquakeMagnitude']['MagnitudeValue']
    focal_depth = info['FocalDepth']
    report_image = earthquake['ReportImageURI']
    report_link = earthquake['Web']

    # 建立輸出格式
    summary = f"1. 災害名稱: {disaster_name}\n"
    summary += f"2. 震央: {epicenter}\n"
    summary += f"3. 震度: {intensity['ShakingArea'][0]['AreaIntensity']}\n"
    summary += f"4. 地震規模: {magnitude}\n"
    summary += f"5. 震源深度: {focal_depth} 公里\n"
    summary += f"8. 報告圖片: {report_image}\n"
    summary += f"9. 報告連結: {report_link}\n\n"

    # 地震震度資訊
    summary += "地震震度資訊:\n"
    for area in intensity['ShakingArea']:
        area_desc = area['AreaDesc']
        county_name = area['CountyName']
        area_intensity = area['AreaIntensity']
        summary += f"- {county_name} ({area_desc}): 震度 {area_intensity}\n"

        for station in area.get('EqStation', []):
            station_name = station['StationName']
            station_intensity = station['SeismicIntensity']
            epicenter_distance = station['EpicenterDistance']

            # 檢查 PGA 和 PGV 是否存在
            pga = None
            pgv = None
            if 'pga' in station:
                pga = max(station['pga'].get('EWComponent', 0),
                          station['pga'].get('NSComponent', 0),
                          station['pga'].get('VComponent', 0))
            if 'pgv' in station:
                pgv = max(station['pgv'].get('EWComponent', 0),
                          station['pgv'].get('NSComponent', 0),
                          station['pgv'].get('VComponent', 0))

            summary += f"  - 測站: {station_name}, 震度: {station_intensity}, 距離震央: {epicenter_distance} 公里\n"
            if pga is not None:
                summary += f"    - PGA: {pga} gal\n"
            if pgv is not None:
                summary += f"    - PGV: {pgv} kine\n"
        summary += "\n"

    return summary


def main():

    API_KEY = "CWA-EE23E8EC-9EA9-44E4-BEF0-BE10B4EDE722"
    jdata = fetch_earthquake_data(API_KEY)
    summary = summarize_earthquake_info(jdata)
    print(summary)
    return summary  # 可選，若你要在其他模組取得這個 summary

if __name__ == "__main__":
    main()
