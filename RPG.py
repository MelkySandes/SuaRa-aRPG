import streamlit as st
import datetime as dt
import base64
import random

# ✅ DEVE vir aqui — logo após os imports
st.set_page_config(page_title="Raça da Terra-Média", layout="centered")

# Função para codificar imagem como base64
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Define plano de fundo com imagem local
set_background("background.png")

# Fonte, botões, trilha sonora e efeitos visuais
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap');

        /* Fundo escuro com overlay */
        .stApp {
            background-color: rgba(0, 0, 0, 0.6) !important;
            font-family: 'UnifrakturCook', cursive;
            color: #f1e6c5;
        }

        /* Overlay escurecedor do fundo */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0, 0, 0, 0.5);
            z-index: -1;
        }

        h1, h2, h3 {
            color: #e0c97f;
            text-shadow: 2px 2px 4px #000000;
        }

        .stButton>button {
            background-color: #5a381e;
            color: #f1e6c5;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            font-size: 1.1em;
            animation: glow 2s infinite;
            transition: transform 0.2s ease;
        }

        .stButton>button:hover {
            transform: scale(1.05);
        }

        @keyframes glow {
            0% { box-shadow: 0 0 5px #ffeaa7; }
            50% { box-shadow: 0 0 20px #ffeaa7; }
            100% { box-shadow: 0 0 5px #ffeaa7; }
        }

        /* Partículas mágicas */
        .magic-particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            background: url('https://www.transparenttextures.com/patterns/stardust.png');
            opacity: 0.15;
            z-index: -2;
            animation: drift 60s linear infinite;
        }

        @keyframes drift {
            0% { background-position: 0 0; }
            100% { background-position: 1000px 1000px; }
        }
    </style>

    <div class="magic-particles"></div>

    <!-- Trilha sonora com autoplay -->
    <audio autoplay loop>
        <source src="https://cdn.pixabay.com/audio/2022/03/15/audio_872e56a939.mp3" type="audio/mpeg">
    </audio>

    <!-- Som de clique -->
    <audio id="click-sound">
        <source src="https://cdn.pixabay.com/audio/2022/03/31/audio_1dfbcab75d.mp3" type="audio/mpeg">
    </audio>

    <script>
        const sound = document.getElementById("click-sound");
        function playClickSound() {
            sound.play();
        }

        const observer = new MutationObserver((mutations) => {
            mutations.forEach(mutation => {
                if (mutation.addedNodes.length > 0) {
                    const btn = document.querySelector("button[kind='primary']");
                    if (btn && !btn.classList.contains('click-bound')) {
                        btn.addEventListener("click", playClickSound);
                        btn.classList.add('click-bound');
                    }
                }
            });
        });

        observer.observe(document.body, { childList: true, subtree: true });
    </script>
""", unsafe_allow_html=True)


# Inicializa sessão
if 'mostrar_resultado' not in st.session_state:
    st.session_state.mostrar_resultado = False

# Funções
def calcular_idade(ano_nascimento):
    try:
        return dt.datetime.now().year - int(ano_nascimento)
    except ValueError:
        return None

def determinar_raca():
    racas = ['⚔️ ORC' '- Fique parado mestre… assim não consigo CORTAR A SUA CABEÇA', '🏹 ELFO ''- bal´a dash,malanore', '🧑‍🎤 HUMANO''- Nenhum rei reina para sempre', '⛏️ ANÃO''- Tempo é dinheiro', '🛑 TROLL''- Vudú é pra Jacú',]
    return random.choice(racas)

# Imagens para cada raça
imagens_raca = {
    '⚔️ ORC''- Fique parado mestre… assim não consigo CORTAR A SUA CABEÇA': 'orc.png',
    '🏹 ELFO''- bal´a dash,malanore': 'elfo.jpg',
    '🧑‍🎤 HUMANO''- Nenhum rei reina para sempre': 'humano.jpg',
    '⛏️ ANÃO''- Tempo é dinheiro': 'anao.jpg',
    '🛑 TROLL''- Vudú é pra Jacú': 'troll.jpg',
}

# Página de resultado
if st.session_state.mostrar_resultado:
    st.markdown("## 🕯️ Revelação dos Ancestrais")
    st.markdown(f"### ✨ *Elen síla lúmenn omentielvo, {st.session_state.nome}!*")

    idade = calcular_idade(st.session_state.ano_nascimento)
    raca = determinar_raca()

    if idade < 17:
        frase = "🍼 Largue a fralda e depois volte aqui!"
    elif 17 <= idade <= 24:
        frase = "🗡️ Muito bem, você já deve servir para alguma coisa."
    elif 25 <= idade <= 40:
        frase = "🛡️ UAU! Enfim alguém destemido e digno de uma jornada."
    else:
        frase = "📜 Volte pra casa, velhote."

    st.markdown(f"**Idade estimada:** {idade} anos — {frase}")
    st.markdown(f"""
        <div class="gold-glow">
          <h2>✨ Você é um {raca}! </h2>
        </div>
    """, unsafe_allow_html=True)

    # Exibe a imagem da raça
    st.image(imagens_raca[raca], caption=f"{raca}", use_container_width=True)

    with open('clientes.csv', 'a', encoding='utf8') as arquivo:
        arquivo.write(f'{st.session_state.nome},{st.session_state.comida},{st.session_state.ano_nascimento},{st.session_state.cor},{st.session_state.atividade_fisica},{st.session_state.temperamento},{st.session_state.tipo_cliente},{raca}\n')

    if st.button("🔁 Voltar à Taverna"):
        st.session_state.mostrar_resultado = False
        st.rerun()

# Página inicial
else:
    st.title('🏰 Qual sua raça na Terra-Média?')
    st.markdown("### 📖 *Até o menor dos hobbits pode moldar o destino do mundo.*")

    nome = st.text_input('📜 Digite seu nome')
    comida = st.text_input('🥘 Sua comida favorita')
    ano_nascimento = st.text_input('🕰️ Seu ano de nascimento', max_chars=4)
    if ano_nascimento and (not ano_nascimento.isdigit() or len(ano_nascimento) != 4):
        st.markdown("<h1 style='color: red; text-align: center;'>VOCÊ É BURRO DE MAIS, NÃO SERVE PARA ESSA AVENTURA!</h1>", unsafe_allow_html=True)
        st.stop()

    cor = st.text_input('🎨 Sua cor preferida')
    atividade_fisica = st.selectbox('⚔️ Sua atividade física', ['Corrida', 'Musculação', 'Vídeo Game', 'Comer', 'Dormir'])
    temperamento = st.selectbox('💭 Seu temperamento', ['Calmo', 'Raivoso', 'Elétrico', 'Observador', 'Tagarela', 'Depressivo'])
    tipo_cliente = st.selectbox('🧝‍♂️ Gênero', ['Homem', 'Mulher', 'Gay'])

    if st.button('🔮 Invocar Resposta'):
        idade = calcular_idade(ano_nascimento)
        if idade is None:
            st.error('⚠️ Ano de nascimento inválido!')
        else:
            st.session_state.nome = nome
            st.session_state.comida = comida
            st.session_state.ano_nascimento = ano_nascimento
            st.session_state.cor = cor
            st.session_state.atividade_fisica = atividade_fisica
            st.session_state.temperamento = temperamento
            st.session_state.tipo_cliente = tipo_cliente
            st.session_state.mostrar_resultado = True
            st.rerun()
