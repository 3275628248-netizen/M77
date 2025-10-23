import os
import json
import requests
from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

class AIModel:
    def __init__(self):
        self.config = self.load_config()
        
    def load_config(self):
        try:
            with open('config.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {"api_key": "demo-mode", "model": "demo"}
    
    def save_config(self):
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
    
    def chat(self, message):
        return self.generate_demo_response(message)
    
    def generate_demo_response(self, user_message):
        user_message_lower = user_message.lower()
        
        if any(word in user_message_lower for word in ['金融', '投资', '股票', '基金', '理财']):
            responses = [
                "基于历史数据分析，建议关注科技和新能源板块的长期投资价值。",
                "当前市场环境下，分散投资是降低风险的有效策略。可以考虑60%股票+30%债券+10%现金的配置。",
                "根据量化模型分析，中小盘成长股在当前估值水平下具有较好的投资机会。",
                "建议建立投资组合：40%指数基金 + 30%行业ETF + 20%个股 + 10%现金备用。"
            ]
        elif any(word in user_message_lower for word in ['你好', '嗨', 'hello', 'hi']):
            responses = [
                "你好！我是金融科技AI助手，很高兴为您服务。",
                "您好！我可以帮助您分析投资策略、风险评估和资产配置建议。",
                "嗨！欢迎使用智能投顾系统，请问有什么可以帮您？"
            ]
        elif any(word in user_message_lower for word in ['风险', '安全', '保守']):
            responses = [
                "根据您的风险偏好，建议配置：20%股票型基金 + 50%债券基金 + 30%货币基金。",
                "保守型投资组合年化收益预计4-6%，最大回撤控制在5%以内。",
                "风险评估模型显示，当前债券市场具有较好的安全边际。"
            ]
        elif any(word in user_message_lower for word in ['收益', '赚钱', '回报']):
            responses = [
                "进取型组合历史回测显示年化收益可达12-15%，但需承担20%左右的最大回撤。",
                "平衡型配置预期年化收益8-10%，风险收益比较为合理。",
                "基于机器学习模型，科技和消费行业未来3年成长性较高。"
            ]
        elif any(word in user_message_lower for word in ['技术', '模型', '算法']):
            responses = [
                "本系统采用机器学习算法分析市场数据，结合多因子模型进行投资决策。",
                "我们的AI模型使用LSTM神经网络预测市场趋势，准确率在历史回测中达到68%。",
                "技术架构包括数据采集、特征工程、模型训练和实时推理四个模块。"
            ]
        elif any(word in user_message_lower for word in ['杉创杯', '比赛', '项目']):
            responses = [
                "这是一个基于AI的金融科技项目，使用Flask框架构建的智能投顾演示系统。",
                "项目展示了如何将人工智能技术应用于金融投资决策支持系统。",
                "这个演示系统模拟了智能投顾的核心功能，包括用户交互和投资建议生成。"
            ]
        else:
            responses = [
                "我主要专注于金融投资和财富管理领域的咨询，请问您想了解哪方面的内容？",
                "作为金融科技AI助手，我可以为您提供投资策略、资产配置和风险评估等服务。",
                "您可以问我关于股票、基金、理财规划或风险管理方面的问题。"
            ]
        
        return random.choice(responses)

ai_model = AIModel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({"error": "消息不能为空"}), 400
    
    response = ai_model.chat(user_message)
    return jsonify({"response": response})

@app.route('/api/config', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        data = request.json
        ai_model.config.update(data)
        ai_model.save_config()
        return jsonify({"status": "success"})
    else:
        return jsonify(ai_model.config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
