export type type_veiculos = {
    Name: string;
    Model: string;
    Engine: string;
    NumberOfPassengers: number;
    Autonomia: string;
    Alcance: string;
    Teto?: string;
}

export type veiculosObj ={
    categoria: string,
    items: type_veiculos[] 
  }