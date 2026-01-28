# app.py
# Página web estilo gourmet oscuro para "La Brownería"
# Versión pulida: sin imágenes de producto, con modales elegantes,
# fondo combinado, responsive y lista para pedidos por WhatsApp

from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Brownería | Sabores artesanales que convierten cada bocado en una experiencia unica</title>

    <!-- Tipografías -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600&family=Cormorant+Garamond:wght@400;500&display=swap" rel="stylesheet">

    <style>
        * { box-sizing: border-box; }
        body {
            margin: 0;
            font-family: 'Cormorant Garamond', serif;
            color: #f3e6d8;
            background:
              linear-gradient(rgba(20,12,8,0.85), rgba(20,12,8,0.85)),
              url('https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&w=1600&q=80') center/cover fixed no-repeat;
        }
        header {
            text-align: center;
            padding: 70px 20px 40px;
        }
        header h1 {
            font-family: 'Playfair Display', serif;
            font-size: 3.2rem;
            margin: 0;
        }
        header p {
            margin-top: 12px;
            font-size: 1.1rem;
            letter-spacing: 1px;
            color: #d6c1a5;
        }
        section {
            max-width: 1200px;
            margin: auto;
            padding: 40px 20px 60px;
        }
        section h2 {
            text-align: center;
            font-family: 'Playfair Display', serif;
            font-size: 2.4rem;
            margin-bottom: 50px;
        }
        .productos {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 35px;
        }
        .producto {
            background: linear-gradient(180deg, #2a1a12, #1c110c);
            border-radius: 16px;
            padding: 35px 25px;
            text-align: center;
            cursor: pointer;
            box-shadow: 0 18px 40px rgba(0,0,0,0.6);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .producto:hover {
            transform: translateY(-6px);
            box-shadow: 0 24px 55px rgba(0,0,0,0.7);
        }
        .producto h3 {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            margin-bottom: 12px;
        }
        .producto p {
            font-size: 1rem;
            color: #e0cdb8;
        }
        /* Modal */
        .modal {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.75);
            align-items: center;
            justify-content: center;
            z-index: 10;
        }
        .modal-content {
            background: linear-gradient(180deg, #2b1b13, #1a0f0a);
            border-radius: 18px;
            padding: 35px 30px;
            max-width: 420px;
            width: 90%;
            text-align: center;
            box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        }
        .modal-content h3 {
            font-family: 'Playfair Display', serif;
            font-size: 1.7rem;
            margin-bottom: 15px;
        }
        .modal-content ul {
            list-style: none;
            padding: 0;
            margin: 0 0 25px;
        }
        .modal-content li {
            margin: 8px 0;
            color: #e7d4bd;
        }
        .cerrar {
            background: none;
            border: 1px solid #d6c1a5;
            color: #d6c1a5;
            padding: 10px 22px;
            border-radius: 30px;
            cursor: pointer;
            font-family: 'Playfair Display', serif;
        }
        .cerrar:hover {
            background: #d6c1a5;
            color: #1a0f0a;
        }
        .whatsapp {
            text-align: center;
            padding: 40px 20px 30px;
        }
        .whatsapp a {
            display: inline-block;
            background: linear-gradient(135deg, #25D366, #1ebe5d);
            color: #ffffff;
            padding: 18px 45px;
            border-radius: 40px;
            font-size: 1.1rem;
            text-decoration: none;
            font-weight: 600;
            box-shadow: 0 10px 25px rgba(0,0,0,0.4);
        }
        .redes {
            text-align: center;
            padding-bottom: 60px;
        }
        .redes a {
            margin: 0 14px;
            color: #d6c1a5;
            font-size: 1.1rem;
            text-decoration: none;
            font-family: 'Playfair Display', serif;
        }
        footer {
            text-align: center;
            padding: 30px 20px;
            background-color: #120a06;
            color: #bfa88e;
            font-size: 0.9rem;
        }
        @media (max-width: 600px) {
            header h1 { font-size: 3.4rem; }
            section h2 { font-size: 2.9rem; }
        }
    </style>
</head>
<body>

<header>
    <h1>La Brownería</h1>
    <p>Sabores artesanales que convierten cada bocado en una experiencia unica</p>
</header>

<section>
    <h2>Nuestros Productos</h2>
    <div class="productos">
        <div class="producto" onclick="abrirModal('Brownies Gourmet',['Bubulubu','Nutella','Snikers','Ferrero','QuesoEdam'])">
            <h3>Brownies Gourmet</h3>
            <p>Haz clic para personalizar</p>
        </div>
        <div class="producto" onclick="abrirModal('Brownies Clasicos',['Azucar Glas','Nutella','Nuez','Oreo','Chokis'])">
            <h3>Brownies Clasicos</h3>
            <p>Haz clic para personalizar</p>
        </div>
        <div class="producto" onclick="abrirModal('Roles de Canela',['Glaseado','Oreo','Nuez','Cajeta','CarlosV','Avellanas','frutosRojos','Chokis'])">
            <h3>Roles de Canela</h3>
            <p>Sabores y toppings</p>
        </div>
        <div class="producto" onclick="abrirModal('Roles de Canela Gourmet $60',['Turin','Ferrero','Bubulubu','KinderDelice','FresasPisatache'])">
            <h3>Roles de Canela Gourmet</h3>
            <p>Sabores y toppings</p>
        </div>
        <div class="producto" onclick="abrirModal('Fresas con Crema $60',['Crema clásica','Oreo','nuez','Granola','Chokis'])">
            <h3>Fresas con Crema</h3>
            <p>Elige tus extras</p>
        </div>
        <div class="producto" onclick="abrirModal('Fresas con Crema Gourmet',['KinderDelice','Bubulubu','Ferero','Pinguino','HeladoVainilla'])">
            <h3>Fresas con Crema Gourmet</h3>
            <p>Elige tus extras</p>
        </div>
        <div class="producto" onclick="abrirModal('Rebanadas de Pastel',['Chocolatin','Beso de Angel','Tres leches'])">
            <h3>Rebanadas de Pastel</h3>
            <p>Variedad de sabores</p>
        </div>
        <div class="producto" onclick="abrirModal('Cheesecake',['Fresa','Oreo','nutella','Tortuga','Zarzamora'])">
            <h3>Cheesecake</h3>
            <p>Selecciona tu topping</p>
        </div>
    </div>
</section>

<div class="whatsapp">
    <a href="https://wa.me/529371214852" target="_blank">Haz tu pedido por WhatsApp</a>
</div>

<div class="redes">
    <a href="https://www.instagram.com/labrowneriacard" target="_blank">Instagram</a> ·
    <a href="https://www.facebook.com/labrowneriacardenas" target="_blank">Facebook</a>
</div>

<footer>
    © 2026 La Brownería · Repostería Gourmet
</footer>

<!-- Modal -->
<div class="modal" id="modal">
    <div class="modal-content">
        <h3 id="modalTitulo"></h3>
        <ul id="modalLista"></ul>
        <button class="cerrar" onclick="cerrarModal()">Cerrar</button>
    </div>
</div>

<script>
function abrirModal(titulo, items) {
    document.getElementById('modalTitulo').innerText = titulo;
    const lista = document.getElementById('modalLista');
    lista.innerHTML = '';
    items.forEach(i => {
        const li = document.createElement('li');
        li.textContent = i;
        lista.appendChild(li);
    });
    document.getElementById('modal').style.display = 'flex';
}
function cerrarModal() {
    document.getElementById('modal').style.display = 'none';
}
</script>

</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
