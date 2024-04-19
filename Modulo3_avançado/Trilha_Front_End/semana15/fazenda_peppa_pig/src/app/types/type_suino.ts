export type type_suino={
    id?:string,
    Brinco: number,
    BrincoPai: number,
    BrincoMae:  number,
    DataNascimento: Date,
    DataSaida: Date,
    Status: "Ativo"| "Vendido" | "Morto",
    Sexo:  "M" | "F",
}


export type type_suino_peso={
    id?:string,
    suinoBrinco: string,
    suinoPeso:  number,
    DataPesagem: Date,
 
}