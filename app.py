import os
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# =========================================================
# Page Configuration
# =========================================================
st.set_page_config(
    page_title="⚡ DigiLogic Pro — Digital Electronics & Flip-Flop Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# Custom UI Styling (Cyber Glassmorphism & Neon Glow)
# =========================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgba(0, 240, 255, 0.05) 0%, transparent 40%),
                    radial-gradient(circle at 90% 80%, rgba(139, 92, 246, 0.07) 0%, transparent 45%),
                    linear-gradient(135deg, #060913 0%, #0f172a 50%, #060913 100%);
        color: #f8fafc;
    }
    
    /* Header Gradient Banner */
    .hero-banner {
        background: linear-gradient(135deg, rgba(0, 240, 255, 0.15) 0%, rgba(59, 130, 246, 0.1) 50%, rgba(139, 92, 246, 0.15) 100%);
        border: 1px solid rgba(0, 240, 255, 0.3);
        padding: 32px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        backdrop-filter: blur(16px);
        box-shadow: 0 10px 35px -10px rgba(0, 240, 255, 0.2);
    }
    
    .hero-banner h1 {
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0;
        background: linear-gradient(135deg, #00f0ff 0%, #3b82f6 50%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero-banner p {
        font-size: 1.1rem;
        margin-top: 10px;
        color: #94a3b8;
    }

    /* Glass Cards */
    .metric-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 24px;
        border-radius: 16px;
        backdrop-filter: blur(12px);
        margin-bottom: 18px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
        transition: border-color 0.3s ease;
    }
    
    .metric-card:hover {
        border-color: rgba(0, 240, 255, 0.4);
    }
    
    /* Digital LED Indicator */
    .led-high {
        display: inline-block;
        width: 22px;
        height: 22px;
        background-color: #00ff88;
        border-radius: 50%;
        box-shadow: 0 0 18px #00ff88, 0 0 35px #00ff88;
        vertical-align: middle;
        margin-right: 8px;
    }
    
    .led-low {
        display: inline-block;
        width: 22px;
        height: 22px;
        background-color: #ef4444;
        border-radius: 50%;
        box-shadow: 0 0 12px rgba(239, 68, 68, 0.6);
        vertical-align: middle;
        margin-right: 8px;
    }

    /* Code & Logic Expressions */
    .logic-pill {
        background: rgba(0, 240, 255, 0.1);
        color: #00f0ff;
        padding: 6px 14px;
        border-radius: 20px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 1rem;
        font-weight: 600;
        border: 1px solid rgba(0, 240, 255, 0.3);
        display: inline-block;
    }

    .badge-tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
        background: rgba(139, 92, 246, 0.15);
        color: #a78bfa;
        border: 1px solid rgba(139, 92, 246, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# Sidebar Navigation & Quick Links
# =========================================================
with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/circuit.png", width=70)
    st.markdown("## ⚡ DigiLogic Pro")
    st.caption("Next-Gen Digital Electronics & Sequential Logic Lab")
    
    st.markdown("---")
    
    module = st.radio(
        "Navigate Lab Modules:",
        [
            "🌐 Web App (Full Visual Suite)",
            "⚡ Logic Gate Simulator",
            "🔁 Sequential Flip-Flop Lab",
            "🧩 MSI Circuits (MUX / DEMUX / Decoders)",
            "📝 MCQ Quiz Arena",
            "📚 Digital Logic Cheat Sheet",
        ],
        index=0
    )
    
    st.markdown("---")
    st.markdown("### 💡 Quick IC Pinout Guide")
    st.markdown("""
    - **AND Gate:** `IC 7408`
    - **OR Gate:** `IC 7432`
    - **NOT Gate:** `IC 7404`
    - **NAND Gate:** `IC 7400`
    - **NOR Gate:** `IC 7402`
    - **XOR Gate:** `IC 7486`
    - **MUX 8:1:** `IC 74151`
    - **Decoder 3:8:** `IC 74138`
    - **Dual JK FF:** `IC 7476`
    - **Dual D FF:** `IC 7474`
    """)
    st.markdown("---")
    st.caption("🚀 Designed by Tanish | Streamlit Cloud Ready")

# =========================================================
# Banner Header
# =========================================================
st.markdown("""
<div class="hero-banner">
    <h1>⚡ DigiLogic Pro — Digital Electronics Hub</h1>
    <p>Simulate logic gates, test combinational circuits, and analyze sequential flip-flop states in real time.</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# Module 1: Full Embedded Web Application
# =========================================================
if module == "🌐 Web App (Full Visual Suite)":
    st.subheader("🌐 Interactive Web Application")
    st.write("Experience the complete animated UI with interactive SVG diagrams, dynamic simulators, quizzes, and responsive themes.")
    
    html_path = os.path.join(os.path.dirname(__file__), "cppsdeco.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=1050, scrolling=True)
    else:
        st.warning("⚠️ `cppsdeco.html` not found in root directory. You can still explore the native Streamlit interactive modules via the sidebar!")

# =========================================================
# Module 2: Native Logic Gate Simulator
# =========================================================
elif module == "⚡ Logic Gate Simulator":
    st.subheader("⚡ Live Logic Gate Simulator")
    st.write("Select a gate, toggle binary inputs $A$ and $B$, and inspect the computed output with real-time truth table highlighting.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("#### 🎛️ Gate Control Center")
        gate_type = st.selectbox("Select Logic Gate Architecture:", ["AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR"])
        
        c_in1, c_in2 = st.columns(2)
        with c_in1:
            input_a = st.selectbox("Input A:", [0, 1], index=0, key="sim_a")
        with c_in2:
            if gate_type == "NOT":
                input_b = None
                st.info("Input B: N/A for single-input inverter")
            else:
                input_b = st.selectbox("Input B:", [0, 1], index=0, key="sim_b")
                
        # Gate Logic Evaluation
        def eval_gate(a, b, g_type):
            if g_type == "AND":
                return a & b, "Y = A · B", "7408"
            elif g_type == "OR":
                return a | b, "Y = A + B", "7432"
            elif g_type == "NOT":
                return 1 if a == 0 else 0, "Y = A̅", "7404"
            elif g_type == "NAND":
                return 0 if (a & b) else 1, "Y = (A · B)̅", "7400"
            elif g_type == "NOR":
                return 0 if (a | b) else 1, "Y = (A + B)̅", "7402"
            elif g_type == "XOR":
                return a ^ b, "Y = A ⊕ B", "7486"
            elif g_type == "XNOR":
                return 1 if a == b else 0, "Y = (A ⊕ B)̅", "74266"
            return 0, "", ""

        output_y, expr, ic_num = eval_gate(input_a, input_b if input_b is not None else 0, gate_type)
        
        st.markdown("---")
        st.markdown(f"**Boolean Expression:** <span class='logic-pill'>{expr}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='badge-tag'>IC {ic_num}</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("#### 💡 Output Status")
        
        led_html = f'<div class="{"led-high" if output_y == 1 else "led-low"}"></div> <strong style="font-size: 1.4rem;">{"HIGH (1)" if output_y == 1 else "LOW (0)"}</strong>'
        st.markdown(f"**Output Y Signal:** {led_html}", unsafe_allow_html=True)
        st.metric(label=f"{gate_type} Gate Result", value=output_y)
        st.markdown('</div>', unsafe_allow_html=True)

    # Truth Table Generation
    st.markdown("### 📊 Dynamic Truth Table")
    if gate_type == "NOT":
        table_data = [
            {"Input A": 0, "Output Y": 1, "State": "👉 ACTIVE" if input_a == 0 else ""},
            {"Input A": 1, "Output Y": 0, "State": "👉 ACTIVE" if input_a == 1 else ""}
        ]
        df = pd.DataFrame(table_data)
    else:
        combinations = [(0,0), (0,1), (1,0), (1,1)]
        rows = []
        for a, b in combinations:
            res, _, _ = eval_gate(a, b, gate_type)
            active = "👉 ACTIVE" if (a == input_a and b == input_b) else ""
            rows.append({"Input A": a, "Input B": b, "Output Y": res, "State": active})
        df = pd.DataFrame(rows)
    
    st.dataframe(df, use_container_width=True)

# =========================================================
# Module 3: Sequential Flip-Flop Laboratory
# =========================================================
elif module == "🔁 Sequential Flip-Flop Lab":
    st.subheader("🔁 Sequential Flip-Flop State Machine Lab")
    st.write("Flip-Flops are bi-stable multivibrators capable of storing 1 bit of memory. Test state transitions on clock edges.")
    
    if "ff_q" not in st.session_state:
        st.session_state.ff_q = 0
    if "ff_history" not in st.session_state:
        st.session_state.ff_history = [{"Clock": 0, "State": "Init", "Q": 0, "Q_bar": 1}]
        
    ff_type = st.selectbox("Select Flip-Flop Architecture:", ["SR Flip-Flop", "JK Flip-Flop", "D Flip-Flop", "T Flip-Flop"])
    
    col_ctrl, col_state = st.columns([1, 1])
    
    with col_ctrl:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown(f"#### ⚙️ {ff_type} Inputs")
        
        invalid_flag = False
        action_desc = ""
        
        if ff_type == "SR Flip-Flop":
            in_s = st.selectbox("Set (S):", [0, 1], index=0)
            in_r = st.selectbox("Reset (R):", [0, 1], index=0)
            
            if in_s == 0 and in_r == 0:
                next_q = st.session_state.ff_q
                action_desc = "No Change (Memory Hold)"
            elif in_s == 0 and in_r == 1:
                next_q = 0
                action_desc = "Reset to 0"
            elif in_s == 1 and in_r == 0:
                next_q = 1
                action_desc = "Set to 1"
            else:
                next_q = st.session_state.ff_q
                invalid_flag = True
                action_desc = "⚠️ Forbidden / Invalid State (S=R=1)"
                
        elif ff_type == "JK Flip-Flop":
            in_j = st.selectbox("J Input:", [0, 1], index=0)
            in_k = st.selectbox("K Input:", [0, 1], index=0)
            
            if in_j == 0 and in_k == 0:
                next_q = st.session_state.ff_q
                action_desc = "No Change (Hold)"
            elif in_j == 0 and in_k == 1:
                next_q = 0
                action_desc = "Reset to 0"
            elif in_j == 1 and in_k == 0:
                next_q = 1
                action_desc = "Set to 1"
            else:
                next_q = 1 if st.session_state.ff_q == 0 else 0
                action_desc = "Toggle State (Q -> Q̅)"
                
        elif ff_type == "D Flip-Flop":
            in_d = st.selectbox("Data Input (D):", [0, 1], index=0)
            next_q = in_d
            action_desc = f"Data Latch (Next Q = {in_d})"
            
        elif ff_type == "T Flip-Flop":
            in_t = st.selectbox("Toggle Input (T):", [0, 1], index=0)
            next_q = (1 if st.session_state.ff_q == 0 else 0) if in_t == 1 else st.session_state.ff_q
            action_desc = "Toggle State" if in_t == 1 else "Hold State"
            
        st.markdown("---")
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("⏱️ Trigger Clock Pulse", type="primary", use_container_width=True):
                if not invalid_flag:
                    st.session_state.ff_q = next_q
                    clk_num = len(st.session_state.ff_history)
                    st.session_state.ff_history.append({
                        "Clock": clk_num,
                        "State": f"{ff_type}: {action_desc}",
                        "Q": st.session_state.ff_q,
                        "Q_bar": 1 if st.session_state.ff_q == 0 else 0
                    })
                else:
                    st.error("Cannot latch on an invalid condition!")
        with btn_col2:
            if st.button("🔄 Reset State", use_container_width=True):
                st.session_state.ff_q = 0
                st.session_state.ff_history = [{"Clock": 0, "State": "Reset", "Q": 0, "Q_bar": 1}]
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    with col_state:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("#### 💡 Latched Memory Status")
        cur_q = st.session_state.ff_q
        cur_q_bar = 1 if cur_q == 0 else 0
        
        m_col1, m_col2 = st.columns(2)
        m_col1.metric("Output Q", cur_q)
        m_col2.metric("Output Q̅ (Inverted)", cur_q_bar)
        
        st.markdown(f"**State Action:** `{action_desc}`")
        if invalid_flag:
            st.error("⚠️ In an SR Flip-Flop, S and R cannot both be HIGH simultaneously.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 📈 Clock Pulse Timing & State History")
    hist_df = pd.DataFrame(st.session_state.ff_history)
    st.dataframe(hist_df, use_container_width=True)

# =========================================================
# Module 4: MSI Combinational Circuits
# =========================================================
elif module == "🧩 MSI Circuits (MUX / DEMUX / Decoders)":
    st.subheader("🧩 Medium Scale Integration (MSI) Circuits")
    st.write("Explore data selectors, distributors, and decoders used in arithmetic units and memory addressing.")
    
    msi_choice = st.selectbox("Select MSI Device:", ["4:1 Multiplexer (MUX)", "1:4 Demultiplexer (DEMUX)", "2:4 Binary Decoder"])
    
    if msi_choice == "4:1 Multiplexer (MUX)":
        st.markdown("### 4:1 Multiplexer (IC 74151 / 74153)")
        st.markdown("Selects one of 4 input lines based on 2 select lines $(S_1, S_0)$ to route to output $Y$.")
        
        c1, c2, c3, c4 = st.columns(4)
        i0 = c1.selectbox("Input I₀:", [0, 1], index=0)
        i1 = c2.selectbox("Input I₁:", [0, 1], index=1)
        i2 = c3.selectbox("Input I₂:", [0, 1], index=0)
        i3 = c4.selectbox("Input I₃:", [0, 1], index=1)
        
        cs1, cs2 = st.columns(2)
        s1 = cs1.selectbox("Select Line S₁ (MSB):", [0, 1], index=0)
        s0 = cs2.selectbox("Select Line S₀ (LSB):", [0, 1], index=0)
        
        sel_val = (s1 << 1) | s0
        inputs = [i0, i1, i2, i3]
        mux_out = inputs[sel_val]
        
        st.success(f"🎯 Selected Channel: **I{sel_val}** | Output **Y = {mux_out}**")
        st.latex(r"Y = \overline{S_1}\,\overline{S_0}I_0 + \overline{S_1}S_0 I_1 + S_1\overline{S_0}I_2 + S_1 S_0 I_3")

    elif msi_choice == "1:4 Demultiplexer (DEMUX)":
        st.markdown("### 1:4 Demultiplexer")
        st.markdown("Distributes a single input signal $I$ to one of 4 output channels based on select lines $(S_1, S_0)$.")
        
        c_in, c_s1, c_s0 = st.columns(3)
        data_in = c_in.selectbox("Data Input (I):", [0, 1], index=1)
        s1 = c_s1.selectbox("Select S₁:", [0, 1], index=0)
        s0 = c_s0.selectbox("Select S₀:", [0, 1], index=0)
        
        sel_idx = (s1 << 1) | s0
        outputs = [0, 0, 0, 0]
        outputs[sel_idx] = data_in
        
        st.write(f"**Outputs:** `Y0={outputs[0]}`, `Y1={outputs[1]}`, `Y2={outputs[2]}`, `Y3={outputs[3]}`")

    elif msi_choice == "2:4 Binary Decoder":
        st.markdown("### 2:4 Decoder (IC 74138 Type)")
        st.markdown("Decodes a 2-bit binary code $(A, B)$ into 4 mutually exclusive active outputs.")
        
        ca, cb = st.columns(2)
        a_in = ca.selectbox("Input A (MSB):", [0, 1], index=0)
        b_in = cb.selectbox("Input B (LSB):", [0, 1], index=0)
        
        dec_idx = (a_in << 1) | b_in
        dec_outs = [1 if i == dec_idx else 0 for i in range(4)]
        
        st.info(f"Active Output Line: **Y{dec_idx}** is HIGH (1)")
        st.write(f"Outputs: `Y0={dec_outs[0]}`, `Y1={dec_outs[1]}`, `Y2={dec_outs[2]}`, `Y3={dec_outs[3]}`")

# =========================================================
# Module 5: Interactive MCQ Quiz Challenge
# =========================================================
elif module == "📝 MCQ Quiz Arena":
    st.subheader("📝 Digital Logic Quiz & Examination Arena")
    st.write("Test your knowledge across logic gate basics, universal gates, flip-flop timing, and IC specifications.")
    
    quiz_difficulty = st.radio("Choose Difficulty:", ["Easy", "Medium", "Hard"], horizontal=True)
    
    questions = {
        "Easy": [
            ("What is the minimum number of inputs for a standard AND gate?", ["1", "2", "3", "4"], 1),
            ("Which IC is standard for a Quad 2-input AND gate?", ["7400", "7408", "7432", "7486"], 1),
            ("Which gate outputs 1 only when inputs are different?", ["OR", "AND", "XOR", "NOR"], 2)
        ],
        "Medium": [
            ("Which of the following gates is considered a Universal Gate?", ["AND", "OR", "NAND", "XOR"], 2),
            ("How many flip-flops are required to build a Mod-16 counter?", ["2", "4", "8", "16"], 1),
            ("What condition in an SR flip-flop leads to an indeterminate/invalid state?", ["S=0, R=0", "S=0, R=1", "S=1, R=0", "S=1, R=1"], 3)
        ],
        "Hard": [
            ("What is the characteristic equation of a JK Flip-Flop?", ["Q(next) = JQ' + K'Q", "Q(next) = J + K", "Q(next) = J'Q + KQ'", "Q(next) = D"], 0),
            ("Which MSI device is functionally equivalent to a data distributor?", ["Multiplexer", "Demultiplexer", "Priority Encoder", "Magnitude Comparator"], 1),
            ("A T flip-flop can be constructed by tying which inputs of a JK flip-flop together?", ["J and K tied together", "J tied to VCC and K to GND", "J inverted into K", "Clock tied to J"], 0)
        ]
    }
    
    user_answers = []
    curr_q_set = questions[quiz_difficulty]
    
    with st.form("quiz_form"):
        for idx, (q, opts, _) in enumerate(curr_q_set):
            st.markdown(f"**Q{idx+1}: {q}**")
            ans = st.radio(f"Select answer for Q{idx+1}:", opts, key=f"q_{quiz_difficulty}_{idx}", label_visibility="collapsed")
            user_answers.append(opts.index(ans))
            st.markdown("---")
            
        submitted = st.form_submit_button("Submit Quiz Assessment", type="primary")
        
        if submitted:
            score = sum(1 for i, (_, _, corr) in enumerate(curr_q_set) if user_answers[i] == corr)
            total = len(curr_q_set)
            
            if score == total:
                st.balloons()
                st.success(f"🎉 Outstanding! Perfect Score: {score}/{total} (100%)")
            elif score >= total / 2:
                st.info(f"👍 Good Job! You scored: {score}/{total}")
            else:
                st.warning(f"📚 Keep practicing! You scored: {score}/{total}")

# =========================================================
# Module 6: Digital Logic Cheat Sheet
# =========================================================
elif module == "📚 Digital Logic Cheat Sheet":
    st.subheader("📚 Digital Logic Formulas & Excitation Matrix")
    
    tab1, tab2, tab3 = st.tabs(["⚡ Boolean Laws & Theorems", "🔁 Flip-Flop Equations", "📋 Excitation Table Matrix"])
    
    with tab1:
        st.markdown("""
        ### Fundamental Boolean Algebra Laws
        - **Identity Law:** $A \cdot 1 = A, \quad A + 0 = A$
        - **Null / Dominance:** $A \cdot 0 = 0, \quad A + 1 = 1$
        - **Idempotent Law:** $A \cdot A = A, \quad A + A = A$
        - **Complement Law:** $A \cdot \overline{A} = 0, \quad A + \overline{A} = 1$
        - **Involution (Double Inversion):** $\overline{\overline{A}} = A$
        - **De Morgan's First Theorem:** $\overline{A \cdot B} = \overline{A} + \overline{B}$
        - **De Morgan's Second Theorem:** $\overline{A + B} = \overline{A} \cdot \overline{B}$
        - **Distributive Law:** $A + (B \cdot C) = (A + B)(A + C)$
        """)
        
    with tab2:
        st.markdown("""
        ### Flip-Flop Characteristic Equations
        | Flip-Flop | Characteristic Equation | Condition |
        | :--- | :--- | :--- |
        | **SR Flip-Flop** | $Q_{next} = S + \overline{R}Q$ | $S \cdot R = 0$ (No simultaneous 1s) |
        | **JK Flip-Flop** | $Q_{next} = J\overline{Q} + \overline{K}Q$ | All combinations valid |
        | **D Flip-Flop** | $Q_{next} = D$ | Data delay latch |
        | **T Flip-Flop** | $Q_{next} = T \oplus Q = T\overline{Q} + \overline{T}Q$ | Toggle memory cell |
        """)
        
    with tab3:
        st.markdown("""
        ### Excitation Table Matrix (State Transition Lookup)
        Used for sequential state machine and counter synthesis:
        """)
        
        ex_data = {
            "Present State (Qn)": [0, 0, 1, 1],
            "Next State (Qn+1)": [0, 1, 0, 1],
            "S": ["0", "1", "0", "X"],
            "R": ["X", "0", "1", "0"],
            "J": ["0", "1", "X", "X"],
            "K": ["X", "X", "1", "0"],
            "D": ["0", "1", "0", "1"],
            "T": ["0", "1", "1", "0"]
        }
        st.dataframe(pd.DataFrame(ex_data), use_container_width=True)
        st.caption("*(X represents a Don't Care condition)*")

# =========================================================
# Footer
# =========================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; opacity: 0.8; font-size: 0.9rem;">
    ⚡ <b>DigiLogic Pro</b> — Digital Electronics & Computer Organization | 🚀 Streamlit Cloud Ready
</div>
""", unsafe_allow_html=True)
