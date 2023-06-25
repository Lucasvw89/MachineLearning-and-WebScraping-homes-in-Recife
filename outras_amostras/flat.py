import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd


homes_csv = pd.DataFrame([], columns=['tipo', 'bairro', 'preço', 'tamanho', 'quartos', 'banheiros', 'garagens'])


driver = webdriver.Chrome('C:/Users/lucas/chromedriver.exe')
driver.get('https://www.chavesnamao.com.br/flat/pe-recife/')

while True:
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/button').click()
        break
    except:
        pass

for j in range(3):
    for i in range(1, 21):
        print(i, '\n')

        try:
            bairro = driver.find_element(By.XPATH, f'/html/body/div[1]/main/article/div[4]/div[{i}]/span[4]/span[1]/a/address/b').text
        except:
            bairro = 'indisponível'

        print("bairro:", bairro)


        try:
            preco = driver.find_element(By.XPATH, f'/html/body/div[1]/main/article/div[4]/div[{i}]/span[4]/span[1]/a/p/b').text
        except:
            preço = 'indisponível'

        print('preço:', preco)


        try:
            tamanho = driver.find_element(By.XPATH, f'/html/body/div[1]/main/article/div[4]/div[{i}]/span[4]/span[2]/ul/li[1]').text
        except:
            tamanho = 'indisponível'

        print('tamanho:', tamanho)


        try:
            quartos = driver.find_element(By.XPATH, f'/html/body/div[1]/main/article/div[4]/div[{i}]/span[4]/span[2]/ul/li[2]').text
        except:
            quartos = 'indisponível'

        print('quartos:', quartos)


        try:
            banheiros = driver.find_element(By.XPATH, f'/html/body/div[1]/main/article/div[4]/div[{i}]/span[4]/span[2]/ul/li[3]').text
        except:
            banheiros = 'indisponível'

        print('banheiros:', banheiros)


        try:
            garagens = driver.find_element(By.XPATH, f'/html/body/div[1]/main/article/div[4]/div[{i}]/span[4]/span[2]/ul/li[4]').text
        except:
            garagens = 'indisponível'

        print('garagens:', garagens)


        print()
        if 'indisponível' not in [bairro, preco, tamanho, quartos, banheiros, garagens] and '--' not in tamanho and 'Confira' not in preco:
            new_home = pd.DataFrame([['flat', bairro.replace(', Recife', ''), preco, tamanho, int(quartos), int(banheiros), int(garagens)]], columns=['tipo', 'bairro', 'preço', 'tamanho', 'quartos', 'banheiros', 'garagens'])
            homes_csv = pd.concat([homes_csv,new_home], ignore_index=True)


    driver.find_element(By.XPATH, '/html/body/div[1]/main/article/span/a').click()
    time.sleep(0.5)


driver.quit()

print(homes_csv)

homes_csv.to_csv('amostra_de_flat.csv')
