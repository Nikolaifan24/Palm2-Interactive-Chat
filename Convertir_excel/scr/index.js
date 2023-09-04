var XLSX = require("xlsx")


const ExelAJSON = () => {
    const excel = XLSX.readFile(
        "C:\\Users\\nikol\\Documents\\GitHub\\Palm2\\Palm2-Interactive-Chat\\Convertir_excel\\Errores_v1.xlsx"
    )
    var nombreHoja = excel.SheetNames;
    let datos = XLSX.utils.sheet_to_json(excel.Sheets[nombreHoja[0]]);
    console.log(datos);
    const jDatos = []
    for (let i = 0 ; i < datos.length ; i++) {
        const  dato = datos[i];
        console.log(dato);
    }

        const jsonData = JSON.stringify(datos);

        const fs = require("fs");

        fs.writeFile("dato.json", jsonData, (err) => {
            if (err) {
                console.error(err);
            } else {
                console.log("El archivo JSON se ha guardado correctamente");
            }
        });
    
};
ExelAJSON();
