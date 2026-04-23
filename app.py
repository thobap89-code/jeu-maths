import streamlit as st
import random
import time

st.set_page_config(page_title="Le Jeu de Maths de Papa", page_icon="🧮")

# --- STYLE CSS ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; font-size: 20px; background-color: #4CAF50; color: white; }
    
    .success-overlay {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0,0,0,0.7);
        display: flex; justify-content: center; align-items: center;
        z-index: 999999;
    }
    .success-card {
        background-color: white;
        padding: 50px;
        border-radius: 30px;
        text-align: center;
        border: 8px solid #4CAF50;
    }
    /* Style pour harmoniser la taille du signe et des chiffres */
    .calcul-display {
        text-align: center; 
        font-size: 80px; 
        color: #2E4053; 
        font-weight: bold;
        font-family: sans-serif;
    }
    .signe {
        font-size: 60px; /* On réduit un peu la taille du signe par rapport aux chiffres */
        vertical-align: middle;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE DU JEU ---
if 'score' not in st.session_state:
    st.session_state.score = 0
    # On force une soustraction au tout premier lancement pour vérifier que ça marche
    st.session_state.nb1 = 10
    st.session_state.nb2 = 4
    st.session_state.op = '-'
    st.session_state.victoire = False

def nouveau_calcul():
    st.session_state.score += 1
    # On choisit l'opération
    st.session_state.op = random.choice(['+', '-'])
    st.session_state.nb1 = random.randint(1, 10)
    st.session_state.nb2 = random.randint(1, 10)
    
    # Sécurité pour la soustraction (pas de résultat négatif)
    if st.session_state.op == '-' and st.session_state.nb1 < st.session_state.nb2:
        st.session_state.nb1, st.session_state.nb2 = st.session_state.nb2, st.session_state.nb1
    
    st.session_state.victoire = False

# --- INTERFACE ---
st.title("🚀 Défi Maths Rigolo pour Mattéo !")
st.sidebar.write(f"### ⭐ Score : {st.session_state.score}")

symbole = "➕" if st.session_state.op == "+" else "➖"

st.markdown("<h2 style='text-align: center;'>Combien font :</h2>", unsafe_allow_html=True)

# Affichage avec le signe légèrement plus petit pour l'alignement
st.markdown(f"""
    <div class="calcul-display">
        {st.session_state.nb1} <span class="signe">{symbole}</span> {st.session_state.nb2}
    </div>
    """, unsafe_allow_html=True)

reponse = st.number_input("Tapes ta réponse :", step=1, value=0, key="input_champ")

if st.button("Vérifier la réponse !"):
    attendu = st.session_state.nb1 + st.session_state.nb2 if st.session_state.op == '+' else st.session_state.nb1 - st.session_state.nb2
    if reponse == attendu:
        st.session_state.victoire = True
        st.rerun()
    else:
        st.error("Oups ! Essaie encore ! 💪")

# --- POPUP VICTOIRE ---
if st.session_state.victoire:
    st.markdown("""
        <div class="success-overlay">
            <div class="success-card">
                <h1 style='font-size: 50px;'>🎉 BRAVO ! 🎉</h1>
                <p style='font-size: 30px;'>Tu es un champion comme Marco!</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.balloons()
    time.sleep(3)
    nouveau_calcul()
    st.rerun()