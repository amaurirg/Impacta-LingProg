from agenda import Agenda

a1 = Agenda('Rafael', '11-999887766', 'rafael@email.com')
a1.novo_contato('Ana', '11-999888563', 'ana@email.com')
a1.novo_contato('Pedro', '11-955552222', 'pedro@email.com')
a1.novo_contato('Mariana', '21-145145145', 'mariana@email.com')
a1.novo_contato('Gustavo', '11-952525252', 'gustavo@email.com')

# primeiro contato
c1 = a1.contatos[0]
# atualiza telefone principal e adiciona novos telefones
c1.adiciona_telefone('11988776655')
c1.adiciona_telefone('1122332233', 'casa')
c1.adiciona_telefone('1145004588', 'trabalho')
# adiciona novos emails
c1.adiciona_email('ana.matos@empresa.com.br', 'trabalho')

# segundo contato
c2 = a1.contatos[1]
# adiciona novos telefones
c2.adiciona_telefone('11-4477-8877', 'casa')
# adiciona novos emails
c2.adiciona_email('pedro.santos@empresa.com', 'trabalho')

# terceiro contato
c3 = a1.contatos[2]
# adiciona novos telefones
c3.adiciona_telefone('19-562-562-562', 'chacara')
c3.adiciona_telefone('21-951-951-987', 'trabalho-rio')
c3.adiciona_telefone('11-987-963-963', 'trabalho-sp')
# adiciona novos emails
c3.adiciona_email('mari.neves@empresa.com', 'trabalho')
c3.adiciona_email('sakura.chan@gmail.com', 'jogos')

# quarto contato
c4 = a1.contatos[3]
# adiciona novos telefones
c4.adiciona_telefone('11-4477-8877', 'casa')
# adiciona novos emails
c4.adiciona_email('gustavo.santos@empresa.com', 'trabalho')

a1.exportar_contatos('exemplo')
