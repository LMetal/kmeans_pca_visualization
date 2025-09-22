import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="PCA & Clustering", layout="wide")

st.title("📊 Visualizzazione PCA multipla")

# --- Sidebar ---
st.sidebar.title("Opzioni")
pickle_choice = st.sidebar.radio(
    "Scegli dataset:",
    ["pca_results_4cl.pkl", "pca_results_5cl.pkl", "pca_results_6cl.pkl"]
)
show_centroids = st.sidebar.checkbox("Mostra centroidi", value=True)
point_size = st.sidebar.slider("Dimensione punti", 3, 12, 6)
centroid_size = st.sidebar.slider("Dimensione centroidi", 8, 20, 14)
legend_font_size = st.sidebar.slider("Dimensione legenda", 12, 30, 18)
color_by_depth = st.sidebar.checkbox("Colore in base alla profondità (z)", value=False)

# --- Carica i dati dal pickle scelto ---
with open(pickle_choice, "rb") as f:
    data = pickle.load(f)

components = data["components"]
y_real = data["y_real"]
centroid_coords = data["centroid_coords"]
labels_assign = data["labels_assign"]
cluster_labels = data["cluster_labels"]

# --- Funzione per gestire la legenda ---
def common_legend_layout(fig):
    fig.update_layout(
        legend=dict(
            orientation="h",
            xanchor="center",
            x=0.5,
            yanchor="top",
            y=1.1,
            font=dict(size=legend_font_size),
            itemsizing="constant"
        ),
        scene=dict(
            camera=dict(projection=dict(type="perspective"))  # 🔑 prospettiva realistica
        )
    )
    return fig

# --- Grafico PCA per Family ---
st.subheader(f"PCA 3D - Punti per Family ({pickle_choice})")
fig1 = go.Figure()
for family in np.unique(y_real):
    mask = (y_real == family)
    fig1.add_trace(go.Scatter3d(
        x=components[mask, 0],
        y=components[mask, 1],
        z=components[mask, 2],
        mode="markers",
        marker=dict(
            size=point_size,
            opacity=0.8,
            color=components[mask, 2] if color_by_depth else None,  # opzionale
            colorscale="Viridis" if color_by_depth else None
        ),
        name=family
    ))
if show_centroids:
    fig1.add_trace(go.Scatter3d(
        x=centroid_coords[:, 0],
        y=centroid_coords[:, 1],
        z=centroid_coords[:, 2],
        mode="markers",
        marker=dict(size=centroid_size, color="red", symbol="x", opacity=1.0),
        name="Centroidi"
    ))
fig1.update_layout(
    title="PCA 3D - Punti per Family",
    scene=dict(xaxis_title="PC1", yaxis_title="PC2", zaxis_title="PC3"),
    height=800
)
fig1 = common_legend_layout(fig1)
st.plotly_chart(fig1, use_container_width=True)

# --- Grafico PCA per Cluster ---
st.subheader(f"PCA 3D - Punti per Cluster ({pickle_choice})")
fig2 = go.Figure()
n_clusters = centroid_coords.shape[0]
for cluster_id in range(n_clusters):
    class_name = cluster_labels[cluster_id]
    legend_name = f"{class_name} (cluster {cluster_id})"
    points_idx = np.where(labels_assign == cluster_id)[0]
    fig2.add_trace(go.Scatter3d(
        x=components[points_idx, 0],
        y=components[points_idx, 1],
        z=components[points_idx, 2],
        mode="markers",
        marker=dict(
            size=point_size,
            opacity=0.8,
            color=components[points_idx, 2] if color_by_depth else None,
            colorscale="Viridis" if color_by_depth else None
        ),
        name=legend_name
    ))
if show_centroids:
    fig2.add_trace(go.Scatter3d(
        x=centroid_coords[:, 0],
        y=centroid_coords[:, 1],
        z=centroid_coords[:, 2],
        mode="markers",
        marker=dict(size=centroid_size, color="red", symbol="x", opacity=1.0),
        name="Centroidi"
    ))
fig2.update_layout(
    title="PCA 3D - Cluster + Centroidi",
    scene=dict(xaxis_title="PC1", yaxis_title="PC2", zaxis_title="PC3"),
    height=800
)
fig2 = common_legend_layout(fig2)
st.plotly_chart(fig2, use_container_width=True)
