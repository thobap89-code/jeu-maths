import streamlit as st
import random
import time

# Configuration de la page
st.set_page_config(page_title="Le Jeu de Maths de Papa", page_icon="🧮")

# --- TOUT LE STYLE CSS (Design du jeu et du Popup) ---
st.markdown("""
    <style>
    /* Fond de l'application */
    .main { background-color: #f0f2f6; }
    
    /* Style du bouton "Vérifier" */
    .stButton>button { 
        width: 100%; 
        border-radius: 20px; 
        height: 3em; 
        font-size: 20px; 
        background-color: #4CAF50; 
        color: white !important; 
    }
    
    /* LE POPUP DE VICTOIRE (Celui qui s'affiche au milieu) */
    .success-overlay {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0,0,0,0.8); /* Fond bien sombre derrière pour faire ressortir le message */
        display: flex; justify-content: center; align-items: center;
        z-index: 999999;
    }
    
    .success-card {
        background-color: #ffffff !important; /* Force le fond blanc pur */
        padding: 40px;
        border-radius: 30px;
        text-align: center;
        border: 8px solid #4CAF50;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
        min-width: 300px;
    }
    
    /* Couleurs forcées pour la lisibilité sur téléphone */
    .success-card h1 {
        color: #1e7b1e !important; /* Vert foncé pour le BRAVO */
        font-size: 45px !important;
        margin-bottom: 10px !important;
    }
    
    .success-card p {
        color: #000000 !important; /* Noir pur pour le texte */
        font-size: 25px !important;
        font-weight: bold !important;
    }

    /* Affichage du calcul */
    .calcul-display {
        text-align: center; 
        font-size: 80px; 
        color: #2E4053; 
        font-weight: bold;
    }
    .signe {
        font-size: 55px; /* Signe un peu plus petit pour l'alignement */
        vertical-align: middle;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE DU JEU (Mémoire du score et des chiffres) ---
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.nb1 = 10
    st.session_state.nb2 = 4
    st.session_state.op = '-'
    st.session_state.victoire = False

def nouveau_calcul():
    st.session_state.op = random.choice(['+', '-'])
    st.session_state.nb1 = random.randint(1, 10)
    st.session_state.nb2 = random.randint(1, 10)
    if st.session_state.op == '-' and st.session_state.nb1 < st.session_state.nb2:
        st.session_state.nb1, st.session_state.nb2 = st.session_state.nb2, st.session_state.nb1
    st.session_state.victoire = False

# --- INTERFACE VISIBLE ---
st.title("🚀 Défi Maths Rigolo pour Mattéo !")
st.sidebar.write(f"### ⭐ Score : {st.session_state.score}")

symbole = "➕" if st.session_state.op == "+" else "➖"

st.markdown("<h2 style='text-align: center; color: #5D6D7E;'>Combien font :</h2>", unsafe_allow_html=True)

st.markdown(f"""
    <div class="calcul-display">
        {st.session_state.nb1} <span class="signe">{symbole}</span> {st.session_state.nb2}
    </div>
    """, unsafe_allow_html=True)

# Champ de réponse (on utilise une clé unique pour le vider plus facilement)
reponse = st.number_input("Tapes ta réponse :", step=1, value=0)

if st.button("Vérifier la réponse !"):
    attendu = st.session_state.nb1 + st.session_state.nb2 if st.session_state.op == '+' else st.session_state.nb1 - st.session_state.nb2
    if reponse == attendu:
        st.session_state.victoire = True
        st.session_state.score += 1
        st.rerun()
    else:
        st.error("Oups ! Essaie encore ! 💪")

# --- LE POPUP DE VICTOIRE ---
if st.session_state.victoire:
    st.markdown("""
        <div class="success-overlay">
            <div class="success-card">
                <h1>🎉 BRAVO ! 🎉</h1>
                <p>Tu es un champion comme Marco! ⛷️ </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.balloons()
    time.sleep(3) # Affiche le message pendant 3 secondes
    nouveau_calcul() # Prépare le prochain calcul
    st.rerun() # Relance l'interface