# Monemotion-Web
Sistema web do projeto Monemotion


Ele possui as seguintes características:

[ainda a serem definidas]

### 📋 Pré-requisitos

- Linux/Windows
- Python 3.9.0
- pip (https://pip.pypa.io/en/stable/)
- virtualenv 

### 🔧 Instalação

1. Instale o virtualenvwrapper:
```bash
sudo apt install python3-pip python-dev build-essential
sudo pip install virtualenv
```

2. Crie um ambiente virtual :

```bash
virtualenv nome_da_virtualenv
```

3. Ativando uma virtualenv:

- Linux ou macOS: 

```bash
source nome_da_virtualenv/bin/activate 
```
- Windows: 

```bash
nome_da_virtualenv/Scripts/Activate 
```

4. Obtenha o código:
```bash
git clone https://github.com/Monemotion/Monemotion-Web.git
```
5. Instale as dependências utilizando o pip:
```bash
pip install -r requirements.txt
```

6. Executar as migrações do proojeto no banco de dados:
```bash
python manage.py migrate
```

7. Executar o projeto:
```bash
python manage.py runserver
```

## 🛠️ Construído com
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src ="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www. python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## ✒️ Autores
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Dfelipe262">
        <img src="https://avatars.githubusercontent.com/u/81752210?v=4" width="100px;" alt="Foto de Damião Felipe no GitHub"/><br>
        <sub>
          <b>Damião Felipe</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/belapf">
        <img src="https://avatars.githubusercontent.com/u/108195377?v=4" width="100px;" alt="Foto de Isabel Freire no GitHub"/><br>
        <sub>
          <b>Isabel Freire</b>
        </sub>
      </a>
    </td>
  </tr>
 
</table>
