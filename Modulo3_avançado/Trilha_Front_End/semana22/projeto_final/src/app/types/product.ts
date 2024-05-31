export type type_product={
    _id?: string,
    nome: string,
    capa:string,
    preco: number,
    avaliacoes:number,
    marca: string,
    descricao?:string
    petshop_id?: string,
    quantidade?:number
}

export type type_api_returnAllProducts={
    error: boolean,
    products:type_product[]
}