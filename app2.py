# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 10:21:42 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la aplicación
st.set_page_config(
    page_title="Portafolio - Gobierno Digital",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .header {
        color: #2F4F4F;
        border-bottom: 2px solid #2F4F4F;
        padding-bottom: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #2F4F4F;
        color: white;
        border-radius: 5px;
    }
    .stTextArea textarea {
        min-height: 150px;
    }
    .success-box {
        background-color: #e6f7e6;
        border-left: 5px solid #2E8B57;
        padding: 10px;
        margin: 10px 0;
    }
    .info-box {
        background-color: #e6f3f8;
        border-left: 5px solid #4682B4;
        padding: 10px;
        margin: 10px 0;
    }
    .card {
        background-color: #f8f9fa;
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .footer {
        text-align: center;
        font-size: 0.8em;
        color: #6c757d;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Información personal y vacante
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("<h1 class='header'>Portafolio Profesional</h1>", unsafe_allow_html=True)
    st.markdown("""
    **Candidato:** Javier Horacio Pérez Ricárdez  
    **Celular:** +52 56 1056 4095  
    **Correo:** [jahoperi@gmail.com](mailto:jahoperi@gmail.com)  
    """)
    
with col2:
    st.image("gobierno_digital_1.jpeg", width=150)  # Reemplaza con tu foto profesional

st.markdown("---")
st.markdown("""
### Postulación para: 
**Analista Funcional / Product Owner**  
**Gobierno de México - Coordinación de Estrategia Digital Nacional**  
""")

# Sidebar mejorado
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>Portafolio Gobierno Digital</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h4>Postulación a:</h4>
        <p>Product Owner / Business Analyst</p>
        <h4>Fecha:</h4>
        <p>{}</p>
    </div>
    """.format(datetime.now().strftime('%d/%m/%Y')), unsafe_allow_html=True)
    
    st.markdown("### Navegación")
    seccion = st.radio("Secciones del portafolio:", [
        "1. Requerimientos",
        "2. Mapeo de procesos",
        "3. Criterios de aceptación",
        "4. Backlog",
        "5. Metodologías ágiles",
        "6. Documentación clara"
    ], label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("""
    <div class='footer'>
        <p>Desarrollado por Javier Horacio Pérez Ricárdez</p>
        <p>© 2025 - Todos los derechos reservados</p>
    </div>
    """, unsafe_allow_html=True)

# 1. Requerimientos
if seccion == "1. Requerimientos":
    st.markdown("<h2 class='header'>1. Levantar, analizar y documentar requerimientos</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box'>
        <strong>Habilidad demostrada:</strong> Capacidad para identificar, clasificar y documentar requerimientos funcionales y no funcionales de sistemas digitales.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📌 Instrucciones", expanded=False):
        st.markdown("""
        - Selecciona el tipo de requerimiento (funcional o no funcional)
        - Describe el requerimiento con claridad
        - Ejemplos funcionales: flujos de usuario, interacciones con el sistema
        - Ejemplos no funcionales: rendimiento, seguridad, disponibilidad
        """)
    
    with st.form("form_requerimientos"):
        col1, col2 = st.columns([1, 3])
        with col1:
            tipo = st.selectbox("Tipo de requerimiento", ["Funcional", "No funcional"])
        with col2:
            descripcion = st.text_area("Descripción", placeholder="Describa el requerimiento con claridad...", height=150)
        
        enviado = st.form_submit_button("➕ Agregar requerimiento")

        if enviado and descripcion:
            if "req_df" not in st.session_state:
                st.session_state.req_df = pd.DataFrame(columns=["Tipo", "Descripción", "Fecha"])
            st.session_state.req_df.loc[len(st.session_state.req_df)] = [tipo, descripcion, datetime.now().strftime('%d/%m/%Y %H:%M')]
            st.success("Requerimiento agregado correctamente")

    if "req_df" in st.session_state and not st.session_state.req_df.empty:
        st.markdown("### Listado de Requerimientos")
        st.dataframe(
            st.session_state.req_df.sort_values("Fecha", ascending=False),
            use_container_width=True,
            hide_index=True,
            column_config={
                "Fecha": st.column_config.DatetimeColumn(
                    "Fecha",
                    format="DD/MM/YYYY HH:mm"
                )
            }
        )
        
        # Estadísticas rápidas
        st.markdown("#### Resumen")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total requerimientos", len(st.session_state.req_df))
        with col2:
            st.metric("Proporción funcionales", 
                      f"{len(st.session_state.req_df[st.session_state.req_df['Tipo'] == 'Funcional'])/len(st.session_state.req_df)*100:.0f}%")
    else:
        st.info("No hay requerimientos registrados aún. Agrega el primero usando el formulario arriba.")

# 2. Mapeo de procesos
elif seccion == "2. Mapeo de procesos":
    st.markdown("<h2 class='header'>2. Mapear, modelar y optimizar procesos</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box'>
        <strong>Habilidad demostrada:</strong> Capacidad para analizar procesos existentes, identificar áreas de mejora y diseñar soluciones optimizadas.
    </div>
    """, unsafe_allow_html=True)
    
    ejemplo_default = """### Proceso actual: Solicitud de Constancia de Situación Fiscal (CSF)

1. **Acceso al portal:** El ciudadano ingresa al portal del SAT
2. **Autenticación:** Inicia sesión con RFC y contraseña (requiere registro previo)
3. **Navegación:** Busca entre múltiples opciones la descarga de CSF
4. **Descarga:** Selecciona formato PDF y descarga manualmente

**Puntos de dolor identificados:**
- Proceso de autenticación complejo
- Navegación poco intuitiva
- No hay opción de envío automático por correo

---

### Proceso optimizado propuesto:

1. **Autenticación simplificada:** 
   - Opción de inicio de sesión con Clave Única de Registro Poblacional (CURP)
   - Integración con gov.mx para autenticación única

2. **Acceso directo:** 
   - Panel principal con acceso destacado a CSF
   - Búsqueda predictiva

3. **Descarga inteligente:**
   - Un solo clic para descarga
   - Opción de envío automático al correo registrado
   - Integración con carpeta ciudadana digital

**Beneficios esperados:**
- Reducción del 70% en tiempo de trámite
- Mejora en satisfacción del usuario
- Disminución de solicitudes de soporte"""
    
    proceso = st.text_area("Documenta el proceso actual y tu propuesta de optimización:", 
                         value=ejemplo_default, 
                         height=400,
                         help="Utiliza markdown para dar formato (## para títulos, **negritas**, listas con - o 1.)")
    
    if st.button("💡 Visualizar propuesta"):
        st.markdown("### Vista previa de la documentación del proceso")
        st.markdown(proceso)
        
        with st.expander("📊 Recomendaciones para presentación ejecutiva", expanded=False):
            st.markdown("""
            - **Incluye métricas:** Tiempos estimados, reducción de pasos, impacto esperado
            - **Diagramas:** Considera añadir flujogramas con herramientas como BPMN
            - **Benchmarking:** Menciona mejores prácticas internacionales
            - **Alcance:** Define claramente qué está dentro y fuera del scope
            """)

# 3. Criterios de aceptación
elif seccion == "3. Criterios de aceptación":
    st.markdown("<h2 class='header'>3. Definir criterios de aceptación</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box'>
        <strong>Habilidad demostrada:</strong> Capacidad para establecer criterios objetivos que permitan validar que una solución cumple con los requerimientos.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🔍 Ejemplo completo", expanded=False):
        st.markdown("""
        **Criterio:** El sistema debe permitir la descarga de la CSF en un solo clic  
        **Validación:**  
        - [x] Botón visible en el dashboard principal  
        - [x] Descarga inicia inmediatamente al hacer clic  
        - [x] Archivo generado es PDF válido  
        - [ ] Tiempo de respuesta menor a 2 segundos  
        """)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        criterio = st.text_input("Criterio de aceptación", 
                               placeholder="El sistema debe...",
                               help="Formato recomendado: 'El sistema debe [acción] para [propósito]'")
    with col2:
        cumple = st.selectbox("Estado de cumplimiento", ["✅ Cumple", "🔄 En progreso", "❌ No cumple"], index=0)
    
    if st.button("💾 Guardar criterio"):
        if not criterio:
            st.warning("Por favor ingresa un criterio antes de guardar")
        else:
            if "criterios" not in st.session_state:
                st.session_state.criterios = []
            st.session_state.criterios.append({
                "criterio": criterio, 
                "cumple": cumple,
                "fecha": datetime.now().strftime('%d/%m/%Y %H:%M')
            })
            st.success("Criterio guardado exitosamente")

    if "criterios" in st.session_state and st.session_state.criterios:
        st.markdown("### Registro de Criterios de Aceptación")
        
        # Convertir a DataFrame para mejor visualización
        df = pd.DataFrame(st.session_state.criterios)
        df = df.sort_values("fecha", ascending=False)
        
        # Mostrar como tabla con estilo
        st.dataframe(
            df[["criterio", "cumple"]],
            use_container_width=True,
            hide_index=True,
            column_config={
                "cumple": st.column_config.TextColumn(
                    "Estado",
                    help="Estado de cumplimiento del criterio"
                ),
                "criterio": st.column_config.TextColumn(
                    "Criterio",
                    help="Descripción del criterio de aceptación"
                )
            }
        )
        
        # Métricas rápidas
        st.markdown("#### Resumen de cumplimiento")
        cumplidos = sum(1 for c in st.session_state.criterios if "✅" in c["cumple"])
        porcentaje = (cumplidos / len(st.session_state.criterios)) * 100
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total criterios", len(st.session_state.criterios))
        col2.metric("Criterios cumplidos", cumplidos)
        col3.metric("Porcentaje cumplido", f"{porcentaje:.0f}%")
        
        # Gráfico de progreso (simple)
        st.progress(int(porcentaje))
    else:
        st.info("No hay criterios registrados aún. Agrega el primero usando el formulario arriba.")

# 4. Backlog
elif seccion == "4. Backlog":
    st.markdown("<h2 class='header'>4. Definir y priorizar el backlog</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box'>
        <strong>Habilidad demostrada:</strong> Capacidad para gestionar el inventario de trabajo priorizando según valor y dependencias.
    </div>
    """, unsafe_allow_html=True)
    
    if "backlog" not in st.session_state:
        st.session_state.backlog = pd.DataFrame(columns=["Funcionalidad", "Prioridad", "Estado", "Sprint", "Fecha"])
    
    with st.expander("📝 Agregar ítem al backlog", expanded=True):
        with st.form("form_backlog"):
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                funcionalidad = st.text_input("Nombre de la funcionalidad", 
                                            placeholder="Descripción breve y clara...")
            with col2:
                prioridad = st.selectbox("Prioridad", ["🔴 Alta", "🟡 Media", "🔵 Baja"], index=0)
            with col3:
                estado = st.selectbox("Estado", ["📋 Por hacer", "✏️ En progreso", "✅ Hecho"], index=0)
            
            sprint = st.selectbox("Sprint/Iteración", ["Sprint 1", "Sprint 2", "Sprint 3", "Por asignar"], index=3)
            
            agregar = st.form_submit_button("➕ Agregar al backlog")

            if agregar and funcionalidad:
                st.session_state.backlog.loc[len(st.session_state.backlog)] = [
                    funcionalidad, 
                    prioridad, 
                    estado,
                    sprint,
                    datetime.now().strftime('%d/%m/%Y %H:%M')
                ]
                st.success("Ítem agregado al backlog")

    if not st.session_state.backlog.empty:
        st.markdown("### Backlog Priorizado")
        
        # Filtros
        col1, col2, col3 = st.columns(3)
        with col1:
            filter_priority = st.multiselect(
                "Filtrar por prioridad",
                options=st.session_state.backlog["Prioridad"].unique(),
                default=st.session_state.backlog["Prioridad"].unique()
            )
        with col2:
            filter_status = st.multiselect(
                "Filtrar por estado",
                options=st.session_state.backlog["Estado"].unique(),
                default=st.session_state.backlog["Estado"].unique()
            )
        with col3:
            filter_sprint = st.multiselect(
                "Filtrar por sprint",
                options=st.session_state.backlog["Sprint"].unique(),
                default=st.session_state.backlog["Sprint"].unique()
            )
        
        # Aplicar filtros
        filtered_backlog = st.session_state.backlog[
            (st.session_state.backlog["Prioridad"].isin(filter_priority)) &
            (st.session_state.backlog["Estado"].isin(filter_status)) &
            (st.session_state.backlog["Sprint"].isin(filter_sprint))
        ]
        
        # Mostrar backlog filtrado
        st.dataframe(
            filtered_backlog.sort_values(["Prioridad", "Estado"]),
            use_container_width=True,
            hide_index=True,
            column_config={
                "Fecha": st.column_config.DatetimeColumn(
                    "Fecha",
                    format="DD/MM/YYYY HH:mm"
                )
            }
        )
        
        # Métricas y visualizaciones
        st.markdown("#### Distribución del backlog")
        tab1, tab2, tab3 = st.tabs(["Por prioridad", "Por estado", "Por sprint"])
        
        with tab1:
            st.bar_chart(filtered_backlog["Prioridad"].value_counts())
        with tab2:
            st.bar_chart(filtered_backlog["Estado"].value_counts())
        with tab3:
            st.bar_chart(filtered_backlog["Sprint"].value_counts())
    else:
        st.info("El backlog está vacío. Agrega el primer ítem usando el formulario arriba.")

# 5. Metodologías ágiles
elif seccion == "5. Metodologías ágiles":
    st.markdown("<h2 class='header'>5. Metodologías ágiles</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box'>
        <strong>Habilidad demostrada:</strong> Conocimiento y aplicación práctica de metodologías ágiles para la gestión de proyectos digitales.
    </div>
    """, unsafe_allow_html=True)
    
    metodo = st.selectbox("Selecciona una metodología para ver detalles:", 
                         ["Scrum", "Kanban", "SAFe", "Design Thinking", "Lean UX"], 
                         index=0)

    if metodo == "Scrum":
        with st.container():
            st.markdown("""
            <div class='card'>
                <h3>🔄 Scrum</h3>
                <p><strong>Mejor para:</strong> Proyectos con requerimientos evolutivos y necesidad de entregas incrementales</p>
                
                <h4>📌 Elementos clave:</h4>
                <ul>
                    <li><strong>Sprints:</strong> Iteraciones de 1-4 semanas con entregable funcional</li>
                    <li><strong>Roles:</strong> Product Owner, Scrum Master, Equipo de Desarrollo</li>
                    <li><strong>Artefactos:</strong> Product Backlog, Sprint Backlog, Incremento</li>
                    <li><strong>Eventos:</strong> Planning, Daily, Review, Retrospective</li>
                </ul>
                
                <h4>🏆 Caso de éxito aplicado:</h4>
                <p>Implementación del módulo de citas en línea para trámites gubernamentales, logrando:</p>
                <ul>
                    <li>Reducción del 40% en tiempos de espera</li>
                    <li>Entregas quincenales de mejoras incrementales</li>
                    <li>Mejora continua mediante retrospectivas efectivas</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
    elif metodo == "Kanban":
        with st.container():
            st.markdown("""
            <div class='card'>
                <h3>📌 Kanban</h3>
                <p><strong>Mejor para:</strong> Equipos de mantenimiento, soporte o flujos de trabajo continuos</p>
                
                <h4>📌 Elementos clave:</h4>
                <ul>
                    <li><strong>Tablero visual:</strong> Columnas que representan estados del flujo de trabajo</li>
                    <li><strong>Límites WIP:</strong> Restricción de trabajo en progreso para evitar sobrecarga</li>
                    <li><strong>Flujo continuo:</strong> No hay sprints, el trabajo fluye constantemente</li>
                    <li><strong>Mejora continua:</strong> Optimización basada en métricas de flujo</li>
                </ul>
                
                <h4>🏆 Caso de éxito aplicado:</h4>
                <p>Gestión del equipo de soporte para el portal de servicios ciudadanos:</p>
                <ul>
                    <li>Visualización clara del trabajo pendiente y en progreso</li>
                    <li>Reducción del 30% en tiempos de resolución</li>
                    <li>Identificación de cuellos de botella mediante métricas de flujo</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
    elif metodo == "SAFe":
        with st.container():
            st.markdown("""
            <div class='card'>
                <h3>🚀 SAFe (Scaled Agile Framework)</h3>
                <p><strong>Mejor para:</strong> Grandes organizaciones con múltiples equipos coordinados</p>
                
                <h4>📌 Elementos clave:</h4>
                <ul>
                    <li><strong>ARTs:</strong> Agile Release Trains - equipos alineados a un valor de negocio</li>
                    <li><strong>PI Planning:</strong> Planificación de incrementos de programa (8-12 semanas)</li>
                    <li><strong>Roles escalados:</strong> Product Management, Release Train Engineer</li>
                    <li><strong>Coordinación:</strong> Sync meetings, Solution Demos</li>
                </ul>
                
                <h4>🏆 Caso de éxito aplicado:</h4>
                <p>Transformación digital de entidad gubernamental con 15 equipos:</p>
                <ul>
                    <li>Alineamiento estratégico mediante PI Plannings bimestrales</li>
                    <li>Coordinación efectiva entre equipos interdependientes</li>
                    <li>Entrega integrada de soluciones complejas</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
    elif metodo == "Design Thinking":
        with st.container():
            st.markdown("""
            <div class='card'>
                <h3>🧠 Design Thinking</h3>
                <p><strong>Mejor para:</strong> Fases iniciales de descubrimiento e innovación</p>
                
                <h4>📌 Elementos clave:</h4>
                <ul>
                    <li><strong>Enfoque centrado en el usuario:</strong> Empatía profunda con necesidades reales</li>
                    <li><strong>Fases:</strong> Empatizar, Definir, Idear, Prototipar, Testear</li>
                    <li><strong>Herramientas:</strong> User personas, journey maps, prototipado rápido</li>
                    <li><strong>Mentalidad:</strong> Apertura a experimentación y fracaso como aprendizaje</li>
                </ul>
                
                <h4>🏆 Caso de éxito aplicado:</h4>
                <p>Rediseño de formularios para trámites de licencias comerciales:</p>
                <ul>
                    <li>Identificación de puntos de dolor mediante observación directa</li>
                    <li>Prototipado rápido y testeos con usuarios reales</li>
                    <li>Reducción del 50% en errores de llenado</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
    elif metodo == "Lean UX":
        with st.container():
            st.markdown("""
            <div class='card'>
                <h3>✂️ Lean UX</h3>
                <p><strong>Mejor para:</strong> Desarrollo de productos digitales con alta incertidumbre</p>
                
                <h4>📌 Elementos clave:</h4>
                <ul>
                    <li><strong>Enfoque en resultados:</strong> Más allá de entregables de diseño</li>
                    <li><strong>Suposiciones:</strong> Identificación y validación temprana</li>
                    <li><strong>Experimentación:</strong> MVP, testeos con usuarios reales</li>
                    <li><strong>Colaboración:</strong> Equipos cross-funcionales co-creando</li>
                </ul>
                
                <h4>🏆 Caso de éxito aplicado:</h4>
                <p>Desarrollo de nueva funcionalidad para declaraciones en línea:</p>
                <ul>
                    <li>Validación temprana de supuestos con usuarios</li>
                    <li>Iteraciones rápidas basadas en feedback real</li>
                    <li>Lanzamiento con 80% menos cambios post-implementación</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    <div class='success-box'>
        <h4>📈 Métricas clave en metodologías ágiles:</h4>
        <ul>
            <li><strong>Velocidad:</strong> Capacidad de entrega por iteración</li>
            <li><strong>Lead Time:</strong> Tiempo desde solicitud hasta entrega</li>
            <li><strong>Satisfacción del equipo:</strong> Health checks periódicos</li>
            <li><strong>Calidad:</strong> Defectos, cobertura de pruebas</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# 6. Documentación clara
elif seccion == "6. Documentación clara":
    st.markdown("<h2 class='header'>6. Documentación clara y estructurada</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box'>
        <strong>Habilidad demostrada:</strong> Capacidad para comunicar información técnica y funcional de manera clara, concisa y estructurada.
    </div>
    """, unsafe_allow_html=True)
    
    tipo_doc = st.selectbox("Selecciona el tipo de documento a redactar:", [
        "Historia de usuario",
        "Documento de requerimientos",
        "Manual de usuario",
        "Reporte de estado",
        "Minuta de reunión"
    ], index=0)
    
    ejemplo_default = {
        "Historia de usuario": """**Historia de usuario:**\n\nComo [rol de usuario], quiero [objetivo/deseo] para [beneficio/valor].\n\n**Criterios de aceptación:**\n- [Criterio 1]\n- [Criterio 2]\n- [Criterio 3]\n\n**Notas:**\n- [Información adicional relevante]\n- [Dependencias técnicas]""",
        
        "Documento de requerimientos": """**Requerimiento:** [ID-001] [Nombre descriptivo]\n\n**Tipo:** Funcional/No funcional\n\n**Descripción:**\n[Descripción detallada del requerimiento]\n\n**Justificación:**\n[Por qué es necesario, qué problema resuelve]\n\n**Prioridad:** Alta/Media/Baja\n\n**Dependencias:**\n- [Requerimiento o sistema relacionado]\n\n**Criterios de éxito:**\n- [Métrica 1]\n- [Métrica 2]""",
        
        "Manual de usuario": """## [Nombre de la funcionalidad]\n\n### Propósito\n[Explicación breve de para qué sirve esta funcionalidad]\n\n### Pasos para usar\n1. [Paso 1 con acciones concretas]\n2. [Paso 2]\n3. [Paso 3]\n\n### Consejos\n- [Tip útil 1]\n- [Tip útil 2]\n\n### Solución de problemas\n**Problema común 1:** [Descripción] -> [Solución]\n**Problema común 2:** [Descripción] -> [Solución]""",
        
        "Reporte de estado": """## Reporte de estado - [Nombre del proyecto/producto]\n\n### Fecha: [DD/MM/AAAA]\n\n### Resumen ejecutivo\n[2-3 orases con lo más importante]\n\n### Avances\n- [Logro 1]\n- [Logro 2]\n\n### Riesgos/Problemas\n1. [Riesgo 1] (Probabilidad: Alta/Media/Baja, Impacto: Alto/Medio/Bajo)\n   - Acciones de mitigación\n2. [Riesgo 2]\n\n### Próximos pasos\n- [Acción 1] (Responsable: [Nombre], Fecha: [DD/MM])\n- [Acción 2]""",
        
        "Minuta de reunión": """## Minuta de reunión\n\n### Fecha y hora: [DD/MM/AAAA] [HH:MM] - [HH:MM]\n\n### Asistentes:\n- [Nombre 1]\n- [Nombre 2]\n\n### Agenda:\n1. [Tema 1]\n2. [Tema 2]\n\n### Acuerdos:\n- [Acuerdo 1] (Responsable: [Nombre], Fecha: [DD/MM])\n- [Acuerdo 2]\n\n### Acciones:\n- [Acción 1] (Responsable: [Nombre], Fecha: [DD/MM])\n- [Acción 2]\n\n### Próxima reunión:\n[DD/MM/AAAA] [HH:MM] - [Tema principal]"""
    }
    
    doc = st.text_area("Redacta tu documento:", 
                      value=ejemplo_default[tipo_doc], 
                      height=400,
                      help="Utiliza markdown para dar formato (## para títulos, **negritas**, listas con - o 1.)")
    
    if st.button("📄 Generar vista previa"):
        st.markdown("### Vista previa del documento")
        st.markdown(doc)
        
        with st.expander("💡 Recomendaciones para documentación efectiva", expanded=False):
            st.markdown("""
            - **Audiencia:** Adapta el lenguaje al público objetivo (técnico, negocio, usuarios finales)
            - **Estructura:** Usa jerarquías claras (títulos, subtítulos)
            - **Concisión:** Ve al punto, evita redundancias
            - **Visuales:** Considera añadir diagramas, screenshots o tablas cuando ayuden
            - **Control de cambios:** Incluye versión, fecha y autor
            - **Glosario:** Define términos técnicos o específicos del dominio
            """)

# Footer principal
st.markdown("---")
st.markdown("""
<div class='footer'>
    <p>Portafolio profesional para postulación a Gobierno Digital</p>
    <p>Última actualización: {}</p>
</div>
""".format(datetime.now().strftime('%d/%m/%Y %H:%M')), unsafe_allow_html=True)