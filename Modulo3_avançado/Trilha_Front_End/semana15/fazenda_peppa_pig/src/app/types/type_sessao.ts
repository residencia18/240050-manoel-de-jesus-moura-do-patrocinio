export type type_sessao={
    id?:string,
    s_date: Date,
    s_description:string,
    animais: [
        {
            suinoBrinco: string,
            atividades: {
                atv_name:"Raiva"| "Rinite_Atrófica" | "Parvovirose_Suína"
                atv_status: boolean
            } 
        }
    ] 
}



