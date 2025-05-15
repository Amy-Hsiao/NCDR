import os, sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger, swag_from
import json
from werkzeug.utils import secure_filename
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__),"./LLM"))
from LLM import main #引用LLM中的整合檔

app = Flask(__name__)
CORS(app)

# Swagger 配置
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "模型整合 API",
        "description": "語言模型與數學模型的 REST API",
        "version": "1.0.0",
        "contact": {
            "name": "API Support",
            "email": "your-email@example.com"
        }
    },
    "basePath": "/api",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ]
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

# 配置文件路徑
DATA_FILE = 'data.json'
RESULT_FOLDER = 'results'

@app.route('/api/language-model', methods=['POST'])
@swag_from({
    'tags': ['語言模型'],
    'summary': '處理語言模型請求',
    'description': '接收提示詞並返回語言模型的回應',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'prompt': {
                        'type': 'string',
                        'description': '輸入的提示詞'
                    }
                },
                'required': ['prompt']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功處理請求',
            'schema': {
                'type': 'object',
                'properties': {
                    'success': {
                        'type': 'boolean',
                        'description': '請求是否成功'
                    },
                    'response': {
                        'type': 'string',
                        'description': '模型的回應'
                    }
                }
            }
        },
        500: {
            'description': '處理請求時發生錯誤',
            'schema': {
                'type': 'object',
                'properties': {
                    'success': {
                        'type': 'boolean',
                        'description': '請求是否成功'
                    },
                    'error': {
                        'type': 'string',
                        'description': '錯誤訊息'
                    }
                }
            }
        }
    }
})
def process_language_model():
    try:
        data = request.json
        query = data.get('prompt', '')
        
        #模型回應
        response = main.main(query)
        
        
        
        return jsonify({
            'success': True,
            'response': response
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500



if __name__ == '__main__':
    app.run(debug=True)