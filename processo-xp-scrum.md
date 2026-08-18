# Processo XP e Scrum — AgileTech Solutions

## 1. Quadro Kanban no GitHub Projects

Para organizar o desenvolvimento do sistema da AgileTech Solutions, foi criado um quadro no GitHub Projects combinando elementos do Scrum e práticas do XP.

O quadro possui as seguintes etapas:

- Backlog
- A Fazer
- Em Desenvolvimento
- Em Revisão
- Concluído

O quadro pode ser acessado pelo link:

[AgileTech Solutions — XP + Scrum](https://github.com/users/Zurg22/projects/1/views/1)

Foram criadas cinco user stories para representar as principais atividades do sistema:

1. Cadastrar usuário
2. Realizar login
3. Criar projeto
4. Criar tarefas no projeto
5. Visualizar tarefas do projeto

Inicialmente, as histórias ficam no Backlog e vão avançando pelas colunas conforme o desenvolvimento acontece.

---

## 2. Práticas de XP adotadas

A equipe da AgileTech Solutions vai utilizar as seguintes práticas do Extreme Programming (XP):

### 2.1 Programação em Pares

Dois desenvolvedores trabalham juntos na mesma tarefa. Enquanto uma pessoa escreve o código, a outra acompanha, revisa e sugere melhorias.

Essa prática ajuda a encontrar erros mais cedo e também facilita o compartilhamento de conhecimento entre os integrantes da equipe.

### 2.2 Desenvolvimento Orientado a Testes (TDD)

Antes ou junto da implementação, a equipe cria testes para verificar o comportamento esperado da funcionalidade.

Isso ajuda a reduzir erros e dá mais segurança para realizar alterações no código.

### 2.3 Integração Contínua

Os desenvolvedores devem integrar suas alterações ao código principal com frequência.

Dessa maneira, os problemas de integração podem ser identificados rapidamente, evitando que várias alterações sejam acumuladas por muito tempo.

### 2.4 Refatoração

A equipe deve melhorar a estrutura do código sempre que necessário, sem alterar o comportamento esperado do sistema.

A ideia é evitar que o código fique desnecessariamente complicado e facilitar sua manutenção.

### 2.5 Design Simples

A equipe deve implementar somente o que realmente é necessário para atender aos requisitos atuais.

Não faz sentido criar funcionalidades apenas imaginando que poderão ser utilizadas no futuro. Essa prática está relacionada ao princípio YAGNI.

### 2.6 Propriedade Coletiva do Código

O código não pertence exclusivamente a um desenvolvedor. Todos os integrantes da equipe podem analisar, alterar e melhorar qualquer parte do sistema.

Isso reduz a dependência de uma única pessoa e facilita a colaboração.

---

## 3. Integração entre XP e Scrum

O Scrum será utilizado principalmente para organizar o trabalho e acompanhar a evolução do produto, enquanto as práticas de XP serão utilizadas durante o desenvolvimento.

O Scrum define uma organização baseada em Sprints, Product Backlog, planejamento, reuniões diárias, Review e Retrospectiva.

O XP complementa esse processo com práticas mais voltadas para a qualidade e para a forma como o código é desenvolvido.

Por exemplo, durante uma Sprint do Scrum, os desenvolvedores podem utilizar programação em pares, TDD, integração contínua, refatoração e design simples.

Dessa forma, Scrum ajuda a equipe a decidir e organizar o que será desenvolvido, enquanto XP ajuda a definir uma forma mais eficiente e segura de desenvolver essas funcionalidades.

---

## 4. Fluxo semanal da equipe

A equipe terá um fluxo de trabalho baseado em Sprints e acompanhamento diário.

### Segunda-feira — Planning

A equipe realiza o planejamento das atividades.

Participam os desenvolvedores e o Product Owner.

Nesse momento, as histórias mais importantes do Product Backlog são analisadas e as tarefas que serão trabalhadas são selecionadas para a Sprint.

### Terça a quinta-feira — Desenvolvimento

Os desenvolvedores trabalham nas tarefas selecionadas.

Durante esse período podem ser utilizadas práticas como:

- Programação em Pares;
- TDD;
- Integração Contínua;
- Refatoração;
- Design Simples.

Também ocorre a Daily Scrum todos os dias.

### Daily Scrum

A Daily é uma reunião rápida, com aproximadamente 15 minutos.

Cada integrante pode informar:

- o que fez desde a última reunião;
- o que pretende fazer;
- se existe algum impedimento.

O objetivo é manter a equipe alinhada e identificar problemas rapidamente.

### Sexta-feira — Review

A equipe apresenta o que foi desenvolvido durante o período para o Product Owner.

O objetivo é verificar se as funcionalidades atendem às necessidades do produto e coletar feedback.

### Sexta-feira — Retrospectiva

Depois da Review, a equipe realiza uma retrospectiva.

Nesse momento são discutidos pontos que funcionaram bem, problemas encontrados e possíveis melhorias para a próxima Sprint.

---

# 5. Cronograma de uma Sprint de 2 semanas

A Sprint terá duração de duas semanas.

| Dia | Atividade | Duração aproximada | Participantes |
|---|---|---:|---|
| Dia 1 | Sprint Planning | 2 horas | Product Owner e desenvolvedores |
| Dias 2 a 4 | Desenvolvimento + XP | Durante o dia | Desenvolvedores |
| Dias 2 a 5 | Daily Scrum | 15 min por dia | Desenvolvedores e Product Owner |
| Dia 5 | Desenvolvimento e integração | Durante o dia | Desenvolvedores |
| Dia 6 | Desenvolvimento + XP | Durante o dia | Desenvolvedores |
| Dia 7 | Desenvolvimento + XP | Durante o dia | Desenvolvedores |
| Dia 8 | Desenvolvimento + testes | Durante o dia | Desenvolvedores |
| Dia 9 | Finalização e preparação da entrega | Durante o dia | Desenvolvedores |
| Dia 10 | Sprint Review | 1 hora | Product Owner e desenvolvedores |
| Dia 10 | Retrospectiva | 45 min | Desenvolvedores e Product Owner |

Durante todos os dias de desenvolvimento, a equipe pode aplicar as práticas de XP conforme a necessidade das tarefas.

---

## 6. Aplicação das práticas XP durante a Sprint

As práticas de XP serão utilizadas ao longo de toda a Sprint.

A programação em pares será utilizada principalmente em tarefas mais complexas ou quando for necessário compartilhar conhecimento entre os desenvolvedores.

O TDD será aplicado nas funcionalidades que exigirem maior controle sobre seu comportamento.

A integração contínua será utilizada sempre que novas alterações forem realizadas no código.

A refatoração será realizada quando a equipe identificar código duplicado, confuso ou desnecessariamente complexo.

O Design Simples será utilizado desde o início para evitar a criação de funcionalidades que não fazem parte dos requisitos atuais.

A propriedade coletiva do código permitirá que qualquer desenvolvedor possa corrigir ou melhorar uma parte do sistema quando necessário.

---

## 7. Entregas esperadas ao final da Sprint

Ao final da Sprint, espera-se que a equipe tenha desenvolvido um incremento funcional do sistema.

Entre as possíveis entregas estão:

- cadastro de usuários;
- login dos usuários;
- criação de projetos;
- criação de tarefas;
- visualização das tarefas;
- código integrado e revisado;
- funcionalidades validadas pelo Product Owner.

A prioridade é entregar software funcionando e que possa ser avaliado, em vez de produzir apenas documentação sobre funcionalidades que ainda não foram implementadas.

---

# 8. Scrum x Kanban

Scrum e Kanban são formas diferentes de organizar o trabalho, mas podem ser utilizados juntos.

| Característica | Scrum | Kanban |
|---|---|---|
| Organização | Trabalha com Sprints | Trabalha com fluxo contínuo |
| Planejamento | Planejamento no início da Sprint | Pode ser feito continuamente |
| Entregas | Normalmente ao final de cada Sprint | Podem acontecer continuamente |
| Reuniões | Possui cerimônias definidas | Não exige cerimônias específicas |
| Papéis | Possui papéis como Product Owner e Scrum Master | Não exige papéis específicos |
| Quadro visual | Pode utilizar quadro | O quadro é um elemento central |
| Quando usar | Quando a equipe precisa trabalhar em ciclos e metas definidas | Quando é importante controlar o fluxo contínuo de tarefas |
| Principal vantagem | Organização por ciclos e objetivos | Visualização e controle do fluxo de trabalho |

## 8.1 Como Scrum e Kanban podem ser combinados

Na AgileTech Solutions, o Scrum será utilizado para organizar o trabalho em Sprints de duas semanas.

O Kanban será utilizado como forma visual de acompanhar o andamento das tarefas.

Assim, o Product Backlog representa o conjunto de necessidades do produto, enquanto o quadro mostra visualmente quais tarefas estão no Backlog, quais serão feitas, quais estão em desenvolvimento, quais estão em revisão e quais já foram concluídas.

Essa combinação permite que a equipe tenha a organização das Sprints do Scrum e, ao mesmo tempo, tenha uma visão clara do fluxo das atividades através do quadro Kanban.