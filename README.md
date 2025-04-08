<body>
    <center>
  <h1 align="center"> Ouvidoria da UniXYZ </h1>
  <br>
      <div align="center">
        </div>

<div align="center">
    <tr>
      <td>
        <ul>
          <li><b>A UniXYZ já te ouvia e tirava suas dúvidas, agora nós também te deixamos a par das manifestações dos outros estudantes. Tudo para que você se sinta mais seguro de conversar e tirar suas dúvidas conosco!</li>
     <br>
<div style="display: flex; gap: 20px; justify-content: center;">
    <img src="https://github.com/user-attachments/assets/16191e18-f2a9-47fc-88b4-0dfc09752940" alt="OUVIDORIAXYZ_capa" style="max-width: 100%; height: auto;">
    <img src="https://github.com/user-attachments/assets/40acdb8c-2bd3-48cd-9518-dcd8a52b60fe" alt="Imagem 2" style="max-width: 100%; height: auto;">
</div>
       </ul>
      </td>
      <td>
      </td>
    </tr>
</div>
              
<br>
              
 <h2>📌 Descrição</h2>
    <p>Este projeto consiste em um sistema de ouvidoria desenvolvido em Python com integração ao banco de dados MySQL. Ele permite registrar, listar, buscar e excluir manifestações, servindo como um projeto didático para o aprendizado de banco de dados e lógica de programação.</p>

 <h2>🛠️ Tecnologias Utilizadas</h2>
 <ul>
 <li><strong>Python</strong>: Linguagem de programação principal utilizada no desenvolvimento</li>
        <li><strong>MySQL</strong>: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar as manifestações.</li>
        <li><strong>Bibliotecas Python</strong>: Utilização de bibliotecas específicas para a conexão e manipulação do banco de dados MySQL.</li>
    </ul>
   <h2>▶️ Como Usar</h2>
    <p>Para utilizar este projeto, siga os passos abaixo:</p>

<h3>1. Clone o repositório</h3>
    <pre><code>git clone https://github.com/marinagv95/Ouvidoria.git</code></pre>

<h3>2. Navegue até o diretório do projeto</h3>
    <pre><code>cd Ouvidoria</code></pre>

<h3>3. Configure o banco de dados MySQL</h3>
    <ul>
        <li>Certifique-se de que o <em>MySQL</em> está instalado e em execução em sua máquina.</li>
        <li>Crie um banco de dados chamado ouvidoria e configure as tabelas conforme o esquema fornecido no arquivo database_schema.txt.</li>
    </ul>

<h3>4. Instale as dependências necessárias</h3>
    <p>Recomenda-se o uso de um ambiente virtual:</p>
    <pre><code>python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate</code></pre>

 <h3>5. Instale as bibliotecas requeridas</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

<h3>6. Configure as credenciais do banco de dados</h3>
    <p>No arquivo operacoesdb.py, insira suas credenciais do MySQL (host, usuário, senha e nome do banco de dados) nas variáveis correspondentes:</p>
    <pre><code>conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="ouvidoria"
)</code></pre>

<h3>7. Execute a aplicação</h3>
    <pre><code>python main.py</code></pre>
    <p>Siga as instruções exibidas no terminal para interagir com o sistema de ouvidoria.</p>

<h2>✅ Funcionalidades</h2>
    <ul>
        <li><strong>Registrar Manifestações</strong>: Permite ao usuário registrar novas manifestações no sistema.</li>
        <li><strong>Listar Manifestações</strong>: Exibe todas as manifestações registradas no banco de dados.</li>
        <li><strong>Buscar Manifestações</strong>: Possibilita a busca de manifestações específicas por meio de critérios definidos.</li>
        <li><strong>Excluir Manifestações</strong>: Permite a remoção de manifestações do sistema.</li>
    </ul>

<h2>📄 Licença</h2>
    <p>Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.</p>
</body>
</html>
<br>
<br>
<br>
<br>


