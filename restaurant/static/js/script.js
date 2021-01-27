if(document.getElementById('menu-categoria')) {
    let valor = document.getElementById('menu-categoria');
    valor.addEventListener('change', function(){
        document.getElementsByTagName('form')[0].submit();
    });
}


