Instalar Python 3
* JDK (JAVA Development Kit): https://www.java.com/pt_BR/download/

* Android Studio: é um pacote do Android Studio que possibilita que possamos instanciar dispositivos móveis de várias configurações e modelos de forma emulada. Para isso, é preciso baixar o Android Studio e, durante o setup, marcar a opção de instalar também o AVD: https://developer.android.com/studio/index.html?hl=pt-br
* Criar Emulador dentro do Android Studio
    - Resolução:
        Preferencialmente dispositivos com resoluções maiores
        Exemplo: Pixel 4(Resolucao 1440 x 3040)
    - Versão de OS:
        Preferencialmente OS mais recentes
        Exemplo: A partir do Androd 9.0
* Instalar .apk no emulador
* Instalar Appium
    - Versão 1.21.0
* Configurar variáveis de ambiente JAVA_HOME e ANDROID_HOME
- Sera descrito duas formas para configurar variaveis de ambiente

*Opcao 1:* abrir no terminal

- Identificar qual nome da pasta java com versao(deve ser identica)
Nesse caminho é possivel saber qual o nome da pasta com a versao que sera utilizada:
    Library/Java/JavaVirtualMachines/jdk1.8.0_171.jdk
        


- Abrir aruqivo bash_profile no terminal atraves do comando:

    open -e ~/.bash_profile
- Inserir no arquivo e salvar:

export ANDROID_HOME=/your/path/to/Android/sdk

export PATH=$ANDROID_HOME/platform-tools:$PATH

export PATH=$ANDROID_HOME/tools:$PATH

export PATH=$ANDROID_HOME/build-tools:$PATH

export JAVA_HOME=/your/path/to/jdk-11.0.12.jdk/Contents/Home

export PATH=$JAVA_HOME/bin:$PATH

*Opcao 2:*

    1- Abra o appium
    2- Edit configuragation
    3- inserir o diretorio do ANDROID_HOME e JAVA_HOME como mostra no exemplo e salve

*Instalar adb*
- Atraves do terminal inserir:

 1- /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)
 
 2- brew install android-platform-tools
 
* ## CHECKLIST DE TUDO QUE É NECESSARIO
Appium Desktop ✔

Android Studio (pacote AVD) ✔

JAVA ✔

IDE ✔

Configuração de variáveis de ambiente ✔

ADB ✔

* ## CONFIGURANDO DESIRED CAPABILITIES
- Acessar o appium e clicar em start Server 
- Clicar na lupa como mostra no exemplo "Start Inspector Session"

- Em desired capabilities os seguintes parametros e valores e Salvar
- platformName(text): Android
- deviceName(text): emulator-5554
- automationName(text): uiautomator2
- appPackage(text): br.com.dudstecnologia.cadastrodeclientes


- Feito isso sua maquina esta preparada para iniciar a sessao para rodar no appium e inspecionar os elementos


* Na raiz do diretório do projeto executar o comando "pip3 install -r requirements.txt"
* Para execucao local ter o app instalado
* ## EXECUTAR TODOS OS TESTES
* Abra o terminal
* Dentro da pasta 'Projeto_Inicio', execute o comando 'behave'