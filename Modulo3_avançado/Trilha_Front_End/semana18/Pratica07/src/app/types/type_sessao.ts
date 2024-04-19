export type type_atividades={
    atv_name:"Raiva"| "Rinite_Atrófica" | "Parvovirose_Suína"
    atv_status: boolean
} 
export type type_sessao={
    id?:string,
    s_date: Date,
    s_description:string,
    s_animais: [
        {
            suinoBrinco: string,
            atividades: type_atividades[]
        }
    ] 
}



