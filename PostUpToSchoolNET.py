#if u not hav 'pip', u can do this command:'wget https://bootstrap.pypa.io/get-pip.py  --no-check-certificate'&'python get-pip.py'
import requests,sys,os,time,json
import urllib.parse
UsrIn=[]
UsrIn=sys.argv
if len(UsrIn) != 3 :
    print('error:pls input ur user&password')
    print('Ag: "python ./PostUpToSchoolNET 10240000 123456')
    exit(1)
if requests.get('http://www.google.cn/generate_204') == '' :
    print('error:NET Is Connect')
    time.sleep(20)
    main()
def Autoping():
    #Linux ping -c ;windows ping -n
    if os.system('ping -c 3 www.google.cn') == 1 :
        main()
    time.sleep(60)
    Autoping()
def main():
    LoginPageUrl=str(requests.get('http://www.google.cn/generate_204').text).split('\'')[1]
    LoginUrl=LoginPageUrl.split('i')[0]+'InterFace.do?method=login'
    QueryString=urllib.parse.quote(LoginPageUrl.split('?')[1])

    Pdata='userId='+UsrIn[1]+'&password='+UsrIn[2]+'&service=&queryString='+QueryString+'&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false'

    Pheaders={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
        'referer':QueryString,
        'cookie':r'EPORTAL_COOKIE_USERNAME=; EPORTAL_COOKIE_PASSWORD=; EPORTAL_COOKIE_SERVER=; EPORTAL_COOKIE_SERVER_NAME=; EPORTAL_AUTO_LAND=; EPORTAL_USER_GROUP=%E5%AD%A6%E7%94%9F%E5%8C%85%E6%9C%88; EPORTAL_COOKIE_OPERATORPWD=;',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    authResult=requests.post(LoginUrl,data=Pdata,headers=Pheaders)
    print(authResult.text)
    authResult=json.loads(authResult.text)
    if authResult['message'] == '' :
        print('NET Link!')
        time.sleep(5)
        Autoping()
    print('NOT Net Link,5555')
    time.sleep(20)
    main()
if __name__ == '__main__':
    #sleep 70s
    #time.sleep(70) #sleep damedame
    main()
