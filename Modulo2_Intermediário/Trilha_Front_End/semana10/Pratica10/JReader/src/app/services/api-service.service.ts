import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { type_veiculos, veiculosObj } from '../../types/types';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  urlToJson = '../assets/veiculos.json';

  private categoriaSubject = new Subject<veiculosObj>();
  private veiculosSubject = new Subject<any>();
  private propriedadeSubject = new Subject<any>();
  private veiculosListSubject = new Subject<string>();


  constructor(private http: HttpClient) {}

  getVeiculos(): Observable<any> {
    return this.http.get(this.urlToJson)
  }

  emitirCategoria(dados: veiculosObj) {
    this.categoriaSubject.next(dados);
  }

  getCategoriaObservable(): Observable<any> {
    return this.categoriaSubject.asObservable();
  }

  emitirVeiculo(dados: type_veiculos) {
    this.veiculosSubject.next(dados);
  }

  getVeiculoObservable(): Observable<type_veiculos> {
    return this.veiculosSubject.asObservable();
  }

  emitirPropriedade(dado: any) {
    this.propriedadeSubject.next(dado);
  }

  getPropObservable(): Observable<string> {
    return this.propriedadeSubject.asObservable();
  }

  emitirListaV(dado: string) {
    this.veiculosListSubject.next(dado);
  }

  getListObservable(): Observable<string> {
    return this.veiculosListSubject.asObservable();
  }




}
