import streamlit as st
import random
import time

# Configuration de la page
st.set_page_config(page_title="Le Jeu de Maths de Papa", page_icon="🧮")

# Style personnalisé pour rendre le jeu plus "enfantin"
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; font-size: 20px; background-color: #4CAF50; color: white; }
    h1 { color: #2E4053; text-align: center; }
    .score { font-size: 24px; font-weight: bold; color: #E74C3C; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Défi Maths Rigolo !")

# Initialisation du score et de l'exercice dans la "session state" (mémoire de la page)
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'nb1' not in st.session_state:
    st.session_state.nb1 = random.randint(1, 20)
    st.session_state.nb2 = random.randint(1, 20)
    st.session_state.operation = random.choice(['+', '-'])
    # S'assurer que la soustraction ne donne pas un résultat négatif
    if st.session_state.operation == '-' and st.session_state.nb1 < st.session_state.nb2:
        st.session_state.nb1, st.session_state.nb2 = st.session_state.nb2, st.session_state.nb1

# Affichage du score
st.sidebar.markdown(f"<p class='score'>Score : {st.session_state.score} ⭐</p>", unsafe_allow_html=True)

# Affichage de la question
st.write(f"## Combien font :")
st.info(f"### {st.session_state.nb1} {st.session_state.operation} {st.session_state.nb2} = ?")

# Zone de réponse
reponse = st.number_input("Tapes ta réponse ici :", step=1, value=0, key="input_reponse")

if st.button("Vérifier !"):
    resultat_attendu = st.session_state.nb1 + st.session_state.nb2 if st.session_state.operation == '+' else st.session_state.nb1 - st.session_state.nb2
    
    if reponse == resultat_attendu:
        st.balloons() # Pluie de ballons !
        st.success("BRAVO ! Tu es un champion ! 🎉")
        st.session_state.score += 1
        time.sleep(2) # Petite pause pour voir le succès
        
        # Générer un nouveau calcul
        st.session_state.nb1 = random.randint(1, 10)
        st.session_state.nb2 = random.randint(1, 10)
        st.session_state.operation = random.choice(['+', '-'])
        if st.session_state.operation == '-' and st.session_state.nb1 < st.session_state.nb2:
            st.session_state.nb1, st.session_state.nb2 = st.session_state.nb2, st.session_state.nb1
        
        st.rerun() # Recharger la page avec le nouveau calcul
    else:
        st.error("Oups ! Essaie encore, tu peux y arriver ! 💪")