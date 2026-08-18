# Processo XP e Scrum — AgileTech Solutions

## 1. Introdução

A AgileTech Solutions possui uma equipe pequena e precisa desenvolver um sistema web de gestão de projetos ágeis. Como os requisitos podem mudar durante o desenvolvimento, a equipe utilizará Scrum para organizar o trabalho e práticas de Extreme Programming (XP) para melhorar a qualidade do desenvolvimento.

O quadro Kanban será utilizado como ferramenta visual para acompanhar o andamento das tarefas durante as Sprints.

---

## 2. Práticas de XP adotadas

A equipe adotará as seguintes práticas de Extreme Programming:

### 2.1 Programação em Pares

Duas pessoas trabalham juntas na mesma tarefa. Uma pessoa escreve o código enquanto a outra acompanha, revisa e sugere melhorias.

Essa prática ajuda a encontrar erros mais cedo e facilita o compartilhamento de conhecimento entre os desenvolvedores.

### 2.2 Desenvolvimento Orientado a Testes (TDD)

Antes de implementar uma funcionalidade, a equipe cria testes que representam o comportamento esperado.

Depois, o código é desenvolvido para fazer os testes passarem. Isso ajuda a reduzir erros e aumenta a confiança nas alterações realizadas.

### 2.3 Integração Contínua

Os desenvolvedores devem integrar suas alterações ao código principal com frequência.

Isso evita que grandes quantidades de código sejam desenvolvidas separadamente por muito tempo e facilita a identificação de conflitos e problemas.

### 2.4 Refatoração

A equipe deve melhorar continuamente a estrutura do código sem alterar o comportamento esperado do sistema.

A refatoração ajuda a manter o código simples, organizado e fácil de manter.

### 2.5 Design Simples

A equipe deve implementar somente o que é realmente necessário para atender aos requisitos atuais.

Essa prática evita complexidade desnecessária e está relacionada ao princípio YAGNI, que significa "You Aren't Gonna Need It".

### 2.6 Propriedade Coletiva do Código

O código pertence à equipe como um todo. Qualquer desenvolvedor pode realizar melhorias ou correções em qualquer parte do sistema.

Isso reduz a dependência de uma única pessoa e facilita a colaboração.

---

## 3. Integração entre XP e Scrum

Scrum será utilizado para organizar e gerenciar o processo de desenvolvimento, enquanto XP será utilizado principalmente para orientar as práticas técnicas da equipe.

O Scrum define eventos, papéis e organização do trabalho. A equipe utilizará Sprints de duas semanas para planejar e entregar incrementos do produto.

Durante essas Sprints, as práticas de XP serão utilizadas no desenvolvimento das funcionalidades.

Por exemplo:

- o Scrum organiza a Sprint e define as prioridades;
- o Product Owner prioriza o Product Backlog;
- o Sprint Planning define o trabalho da Sprint;
- as práticas de XP orientam a implementação;
- o TDD será utilizado durante o desenvolvimento;
- a programação em pares será utilizada em tarefas que possam se beneficiar de revisão conjunta;
- a integração contínua será realizada durante toda a Sprint;
- a refatoração será realizada sempre que necessário;
- o Design Simples será utilizado para evitar funcionalidades desnecessárias;
- ao final da Sprint, o incremento será apresentado na Sprint Review.

Dessa forma, Scrum e XP se complementam: Scrum organiza o trabalho e XP ajuda a garantir qualidade técnica.

---

## 4. Fluxo de trabalho da equipe

A equipe utilizará o seguinte fluxo durante as Sprints:

### Segunda-feira — Planning

A equipe realiza o Sprint Planning para definir o objetivo da Sprint e selecionar os itens prioritários do Product Backlog.

As tarefas selecionadas são colocadas no quadro de acompanhamento.

### Terça-feira a sexta-feira — Desenvolvimento

Os desenvolvedores trabalham nas tarefas selecionadas.

Durante esse período são utilizadas as práticas de XP, como TDD, programação em pares, integração contínua, refatoração e Design Simples.

### Todos os dias — Daily Scrum

A equipe realiza uma reunião rápida de aproximadamente 15 minutos.

Cada integrante informa:

- o que realizou;
- o que pretende fazer;
- se existe algum impedimento.

### Segunda semana — Desenvolvimento e preparação da entrega

A equipe continua o desenvolvimento, realizando testes, integração e correções.

As tarefas concluídas passam por revisão antes de serem consideradas prontas.

### Final da Sprint — Review

A equipe apresenta o incremento desenvolvido ao Product Owner e coleta feedback.

### Final da Sprint — Retrospectiva

Após a Review, a equipe realiza uma retrospectiva para analisar o que funcionou bem, o que poderia melhorar e quais ações serão tomadas na próxima Sprint.

---

## 5. Quadro Kanban no GitHub Projects

O quadro da AgileTech Solutions foi criado no GitHub Projects para acompanhar visualmente o trabalho da equipe.

Link para o quadro:

https://github.com/users/Zurg22/projects/1/views/1

O quadro possui as seguintes etapas:

- Todo;
- In Progress;
- Done.

As tarefas são representadas por Issues do GitHub vinculadas ao projeto.

### User Stories adicionadas

O quadro possui pelo menos cinco itens:

1. **Cadastrar usuário**
   - Como usuário, quero realizar meu cadastro no sistema para poder acessar a plataforma.

2. **Realizar login**
   - Como usuário, quero fazer login com meu e-mail e senha para acessar minha conta.

3. **Criar projeto**
   - Como usuário, quero criar um projeto para organizar minhas atividades e acompanhar seu desenvolvimento.

4. **Criar tarefas no projeto**
   - Como usuário, quero criar tarefas dentro de um projeto para organizar as atividades que precisam ser realizadas.

5. **Visualizar tarefas do projeto**
   - Como usuário, quero visualizar as tarefas do projeto para acompanhar suas atividades.

Esses itens representam funcionalidades que podem ser desenvolvidas durante as Sprints.

---

# 6. Cronograma de uma Sprint de duas semanas

A Sprint terá duração de duas semanas.

| Dia | Atividade | Duração | Participantes |
|---|---|---:|---|
| Dia 1 | Sprint Planning | 2 horas | Scrum Master, Product Owner e desenvolvedores |
| Dias 2 a 4 | Desenvolvimento + Daily | Daily de 15 min | Desenvolvedores e Scrum Master |
| Dia 5 | Desenvolvimento + Daily | Daily de 15 min | Desenvolvedores e Scrum Master |
| Dias 6 a 9 | Desenvolvimento + Daily | Daily de 15 min | Desenvolvedores e Scrum Master |
| Dia 10 | Desenvolvimento, Review e Retrospectiva | Review 1h + Retrospectiva 1h | Toda a equipe e Product Owner na Review |

---

## 7. Aplicação das práticas de XP durante a Sprint

As práticas de XP serão distribuídas durante todo o período da Sprint.

### Dias 1 e 2

A equipe começa as funcionalidades selecionadas no Planning.

O Design Simples será utilizado para evitar funcionalidades que não fazem parte dos requisitos atuais.

### Dias 2 a 9

Durante o desenvolvimento serão utilizadas:

- TDD;
- Programação em Pares;
- Integração Contínua;
- Refatoração;
- Design Simples;
- Propriedade Coletiva do Código.

Os desenvolvedores poderão alternar entre programação individual e programação em pares de acordo com a complexidade das tarefas.

### Dias 8 e 9

A equipe realiza uma revisão das funcionalidades concluídas, corrige problemas e garante que o código esteja integrado.

Também serão realizados testes para verificar se as funcionalidades atendem aos requisitos.

### Dia 10

O incremento desenvolvido será apresentado ao Product Owner durante a Sprint Review.

Após a Review, a equipe realiza a Retrospectiva e identifica melhorias para a próxima Sprint.

---

## 8. Cerimônias do Scrum

### Sprint Planning

Ocorre no primeiro dia da Sprint.

Objetivo: definir o objetivo da Sprint e selecionar os itens que serão desenvolvidos.

Participantes:

- Product Owner;
- Scrum Master;
- desenvolvedores.

Duração planejada: aproximadamente 2 horas.

### Daily Scrum

Ocorre todos os dias úteis da Sprint.

Objetivo: acompanhar o progresso e identificar impedimentos.

Duração: aproximadamente 15 minutos.

Participantes:

- desenvolvedores;
- Scrum Master.

O Product Owner pode participar quando necessário.

### Sprint Review

Ocorre no último dia da Sprint.

Objetivo: apresentar o incremento desenvolvido e receber feedback.

Participantes:

- Product Owner;
- desenvolvedores;
- Scrum Master;
- interessados convidados.

Duração planejada: aproximadamente 1 hora.

### Sprint Retrospective

Ocorre após a Sprint Review.

Objetivo: analisar o processo de trabalho e identificar melhorias.

Participantes:

- Product Owner;
- desenvolvedores;
- Scrum Master.

Duração planejada: aproximadamente 1 hora.

---

# 9. Entregas esperadas ao final da Sprint

Ao final da Sprint, espera-se que a equipe entregue um incremento funcional do sistema.

Entre as possíveis entregas estão:

- cadastro de usuários funcionando;
- login funcionando;
- criação de projetos;
- criação de tarefas;
- visualização das tarefas;
- código integrado;
- funcionalidades testadas;
- código revisado e refatorado quando necessário.

A entrega deve estar em condições de ser apresentada ao Product Owner e avaliada.

---

# 10. Scrum x Kanban

| Característica | Scrum | Kanban |
|---|---|---|
| Organização | Trabalho dividido em Sprints | Fluxo contínuo |
| Planejamento | Realizado no início da Sprint | Pode ocorrer continuamente |
| Entregas | Normalmente ao final da Sprint | Podem ocorrer continuamente |
| Papéis | Possui papéis definidos | Não exige papéis específicos |
| Limite de trabalho | O trabalho é definido para a Sprint | Utiliza limites de trabalho em andamento |
| Quando usar | Quando a equipe precisa de ciclos e objetivos definidos | Quando é importante acompanhar um fluxo contínuo |
| Principal vantagem | Organização por ciclos e objetivos | Visualização e controle do fluxo |
| Mudanças | Podem ser planejadas para próximas Sprints | Podem ser incorporadas ao fluxo conforme disponibilidade |
| Uso no projeto | Organizar a Sprint | Visualizar o andamento das tarefas |

---

## 11. Como Scrum e Kanban podem ser combinados

Scrum e Kanban podem ser utilizados juntos.

Na AgileTech Solutions, o Scrum será responsável por organizar o trabalho em Sprints de duas semanas, definir objetivos e realizar as cerimônias.

O Kanban será utilizado como forma visual de acompanhar o andamento das tarefas.

Assim, o Product Backlog representa o conjunto de necessidades do produto, enquanto o quadro mostra visualmente quais tarefas estão no Todo, quais estão em desenvolvimento e quais já foram concluídas.

Essa combinação permite que a equipe tenha a organização das Sprints do Scrum e, ao mesmo tempo, tenha uma visão clara do fluxo das atividades através do quadro Kanban.

---

## 12. Conclusão

A combinação de Scrum, Kanban e práticas de XP oferece uma forma adequada de organizar o desenvolvimento da AgileTech Solutions.

O Scrum fornece uma estrutura para planejamento, acompanhamento e revisão do trabalho. O Kanban facilita a visualização do fluxo das tarefas. As práticas de XP contribuem para melhorar a qualidade técnica, reduzir erros e manter o código simples.

Com essa abordagem, a equipe consegue trabalhar em ciclos curtos, receber feedback frequente e adaptar o desenvolvimento conforme as necessidades do produto.