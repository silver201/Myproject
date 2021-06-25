from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'first_name': '黄',
    # 'first_name': '111',
    'last_name' : '思雨',
    'sx':'hsy',
    'con':'123 My Place Drive',
    'address' : '湖北师范大学',
    'job': 'Web developer',
    'tel': '0678282923',
    'email': 'sasa07072021@outlook.com',
    # 'description' : 'Suite à une expérience internationale en développement web et dans le domaine des arts, l’impact de l’intelligence artificielle dans nos vies me surprend de jour en jour. \n Aujourd’hui, je souhaite changer de cap et comprendre les secrets que recèlent nos données. J’aimerais mettre à profit ces découvertes au service des entreprises/associations à dimension sociale.',
    'description' : '我待人真诚，工作认真负责；积极主动，能吃苦耐劳，勇于承受压力;有很强团队协作精神，具有较强的适应能力;纪律性强; 意志坚强，具有较强的无私奉献精神。对待工作认真负责，善于沟通；活泼开朗、乐观上进、有爱心；上进心强、勤于学习能不断提高自身的能力与综合素质。在未来的工作中，我将以充沛的精力，刻苦钻研的精神来努力工作，稳定地提高自己的工作能力，与公司同步发展',
    # 'social_media' : [
    'social_media' : [
        {
            'link': '252809',
            'icon' : 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/silver201',
            'icon' : 'fa-github'
        },
        {
            'link': 'sasa0707@outlook.com',
            'icon' : 'fa-linkedin-in'
        }
    ],
    'img': 'img/123.jpg',
    'experiences' : [
        {
            'title' : '记账微信小程序',
            'company': 'AZULIK',
            'description' : '此项目是一个记账的微信小程序，通过微信用户登录实现记账、预算、展示消费图表等功能。项目技术：项目使用微信开发者工具进行开发，数据库使用微信开发者工具自带的云数据 库。本人主要运用node.js编写实现数据库连接并展示消费图表功能、以及wxml实现界面的一些设计。',
            'timeframe' : '2021.03-2021.06'
        },
        {
            'title' : '简易购物商城',
            'company': 'Independant',
            'description' : '网页主要展示了一个小型的购物商城。功能包括登录、注册、商品展示、购物车、个人中心、订单展示等。项目描述：网页采用MVC三层框架，WEB层使用jsp技术,控制转发层使用自定义的Servlet来控制，业务逻辑层使用轻量级的JavaBean,，主要使用html+css进行布局美化， 数据库使用mysql实现对数据的操作。项目成果：完成了页面设计（登录注册、商城展示、下订 单、购物车、订单展示、个人中心）以及页面实现。 ',
            'timeframe' : '2020.09-2020.12'
        }
        # ,
        # {
        #     'title' : 'Sharepoint Intern',
        #     'company': 'ALTEN',
        #     'description' : 'Help to manage a 600 Sharepoint sites platform (audit, migration to Sharepoint newer versions)',
        #     'timeframe' : 'October 2015 - October 2016'
        # }
    ],
    'education' : [
        {
            # 'university': 'Paris Diderot',
            # 'degree': 'Projets informatiques et Startégies d\'entreprise (PISE)',
            # 'description' : 'Gestion de projets IT, Audit, Programmation',
            # 'mention' : 'Bien',
            # 'timeframe' : '2015 - 2016'
            'university': '湖北师范大学',
            # 'degree': 'Projets informatiques et Startégies d\'entreprise (PISE)',
            'degree': '软件工程',
            'description' : '主修课程：C/C++程序设计、数据结构、数据库原理及开发、Java应用开发与实践、Python程序设计基础、软件过程与管理。',
            # 'mention' : 'Bien',
            'timeframe' : '2018 - 2022'
        }
    ],
    'programming_languages' : {
        'HMTL' : ['fa-html5', '100'], 
        'CSS' : ['fa-css3-alt', '100'], 
        'JS' : ['fa-js-square', '90'],
        'Python': ['fa-python', '70'],
        'MySQL' : ['fa-database', '60'],
        'NodeJS' : ['fa-node-js', '50']
    },
    # 'languages' : {'French' : 'Native', 'English' : 'Professional', 'Spanish' : 'Professional', 'Italian' : 'Limited Working Proficiency'},
    'languages' : {'French' : 'Native', 'English' : 'Professional', 'Spanish' : 'Professional', 'Italian' : 'Limited Working Proficiency'},
    'interests' : ['运动', '吃东西', 'Languages']
}

@app.route('/')
def cv(person=person):
    return render_template('index.html', person=person)


@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))


@app.route('/chart')
def index():
	return render_template('chartsajax.html',graphJSON5=gm4(),graphJSON2=gm1())

@app.route('/chart1')
def index1():
	return render_template('chart1.html',graphJSON9=gm8(),graphJSON4=gm3())

def gm1():
	df = pd.DataFrame(px.data.tips())
	fig = px.scatter_matrix(df)
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

def gm3():
	df = pd.DataFrame(px.data.gapminder())
	fig =px.scatter_geo(df, locations="iso_alpha", color="continent", hover_name="country", size="pop",
               animation_frame="year", projection="natural earth")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON


def gm4():
	df = pd.DataFrame(px.data.tips())
	fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

def gm8():
	df = pd.DataFrame(px.data.gapminder())
	fig =px.choropleth(df, locations='iso_alpha', color='lifeExp', hover_name='country', animation_frame='year',
              color_continuous_scale=px.colors.sequential.Plasma, projection='natural earth')
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
