import streamlit as st
import random

st.title("É dia de beber vinho? 🍷")

if st.button("Clique aqui para descobrir"):
    sujeitos = [
        "Os astros alinharam e dizem que",
        "Segundo a tradição milenar,",
        "Um estudo altamente científico prova que",
        "Seu eu do futuro agradece se",
        "A sabedoria popular afirma que",
        "O horóscopo de hoje recomenda que",
        "O vizinho do 402 comentou que",
        "Uma mensagem numa garrafa dizia que",
        "A previsão do tempo indica que",
        "Um pássaro me contou que"
    ]

    motivos = [
        "abrir uma garrafa de vinho",
        "degustar um bom tinto",
        "se deliciar com um vinho branco",
        "apreciar um rosé geladinho",
        "experimentar aquele vinho guardado",
        "brindar com uma taça de vinho",
        "descobrir novos sabores de vinho",
        "compartilhar vinho com amigos",
        "tomar uma taça por conta da saúde",
        "iniciar a coleção de rolhas"
    ]

    justificativas = [
        "traz sorte para o resto da semana.",
        "afasta as energias negativas.",
        "é a chave para a felicidade eterna.",
        "torna você mais interessante.",
        "faz o tempo frio ficar aconchegante.",
        "espanta o tédio e atrai a diversão.",
        "é o segredo dos grandes gênios.",
        "faz os problemas parecerem menores.",
        "é a melhor forma de celebrar a vida.",
        "ajuda na digestão das boas ideias."
    ]

    desculpa = f"{random.choice(sujeitos)} {random.choice(motivos)} {random.choice(justificativas)}"
    st.write(desculpa)
