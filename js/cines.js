const getCines = async ()=>{
    const id = new URLSearchParams( window.location.search ).get('id')
    const data = await fetch(`https://oaemdl.es/cinestar_sweb_php/cines`)
    if ( data.status == 200 ) {
        let cines = await data.json()
        let html = '<br/><h1>Nuestros Cines</h1><br/>'
        cines.data.forEach(cines => {
            html += `
                <div class="contenido-cine">
	        	    <img src="img/cine/${cines.id}.1.jpg" width="227" height="170"/>
            	   	<div class="datos-cine">
       				   	<h4>${cines.RazonSocial}</h4><br/>
                		<span>${cines.Direccion} - ${cines.Distrito}<br/><br/>Teléfono: ${cines.Telefonos}</span>
                	</div>
                	<br/>
                	<a href="cine.html?id=${cines.id}">
                		<img src="img/varios/ico-info2.png" width="150" height="40"/>
                	</a>
				</div>            
            `
        });
        document.getElementById('contenido-interno').innerHTML = html
    }
}
getCines()