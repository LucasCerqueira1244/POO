# Polimorfismo em Python <br>
O polimorfismo em Python refere-se à capacidade de um objeto ser referenciado de várias formas diferentes, permitindo que um mesmo método seja chamado em objetos de classes diferentes. Isso significa que objetos de diferentes classes podem ser tratados de maneira uniforme se compartilharem um método comum.

Exemplo de Polimorfismo na vida real
Um exemplo de polimorfismo da vida real, pode ser uma aplicação bancária que lida com diferentes tipos de contas, como conta corrente, conta poupança e conta de investimento. Embora cada tipo de conta possua características e comportamentos específicos, eles também têm funcionalidades comuns, como depositar e sacar dinheiro.

Nesse exemplo, podemos criar uma classe base chamada "Conta" e, em seguida, derivar outras classes específicas, como "ContaCorrente", "ContaPoupanca" e "ContaInvestimento". Cada uma dessas classes pode ter sua própria implementação dos métodos "depositar" e "sacar", mas todos eles compartilham uma interface comum.

Ao chamar o método "sacar" em objetos do tipo "ContaCorrente" e "ContaPoupanca", o polimorfismo permite que o código trate esses objetos de forma uniforme, mesmo que a implementação real do método seja diferente para cada classe.

O exemplo citado acima estará no arquivo "polimorfismo.py"


# Herança em Python <br>
A herança é um conceito importante na programação orientada a objetos que permite que uma classe herde atributos e métodos de outra classe, chamada de classe pai ou superclasse. A classe que herda é chamada de classe filha ou subclasse. A herança permite a reutilização de código e facilita a organização e a extensão de classes relacionadas.

Quando uma classe herda de outra, ela recebe todos os atributos e métodos da classe pai e pode adicionar ou modificar funcionalidades conforme necessário. A classe filha pode estender a funcionalidade da classe pai ou especializá-la para um contexto específico.

<strong>O exemplo estrá no arquivo "heranca.py"</strong>

Nesse exemplo, temos uma classe base chamada "Pessoa" que possui os atributos nome e idade, além do método exibir_informacoes para mostrar os dados da pessoa. A classe "Estudante" herda da classe "Pessoa" utilizando a sintaxe class Estudante(Pessoa). A classe "Estudante" adiciona um atributo extra chamado matricula e sobrescreve o método exibir_informacoes para incluir também a matrícula.

Ao criar um objeto estudante1 da classe "Estudante", ele herda os atributos e métodos da classe "Pessoa" por meio da herança. O método exibir_informacoes é chamado em estudante1, e a implementação da classe "Estudante" é executada. No entanto, a classe "Estudante" também chama o método exibir_informacoes da classe "Pessoa" usando super().exibir_informacoes(), garantindo que as informações da pessoa sejam exibidas junto com a matrícula.

No exemplo acima, a classe "Estudante" estendeu a funcionalidade da classe "Pessoa" adicionando um novo atributo, mas também poderia ter modificado o comportamento de um método existente ou adicionado métodos novos. A herança permite essa flexibilidade na criação de classes mais especializadas a partir de classes mais genéricas.
