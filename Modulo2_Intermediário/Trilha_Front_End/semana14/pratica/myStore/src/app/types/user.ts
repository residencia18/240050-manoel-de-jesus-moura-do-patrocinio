export type type_user ={
    user_fistName : string,
    user_fullName : string,
    user_password : string,
    user_email : string,
    user_phone : string,
    user_address : string,
    user_birthday : Date|string,
    user_gender : string,
    user_profession : string,
    _token?: string
    _tokenExpirationDate?: Date
}