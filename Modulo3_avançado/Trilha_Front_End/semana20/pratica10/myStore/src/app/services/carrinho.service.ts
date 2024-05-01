import { computed, Injectable, signal } from '@angular/core';
import { type_product } from '../types/product';
import { filter } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CarrinhoService {
  listInicial: type_product[] = [];
  carrinho = signal<type_product[]>(this.listInicial);
  constructor() { }

  addItem(novoProduto: type_product) {
    if (!this.listInicial.includes(novoProduto)) {
      this.listInicial.push({...novoProduto,quantidade: 1});
      this.carrinho.set(this.listInicial)


      console.log("this.listInicial", this.listInicial)
      console.log("this.carrinho", this.carrinho())
    }
  }

  removeItem(produto: type_product) {

    if (this.listInicial.includes(produto)) {
      const novaLista = this.listInicial.filter(item => item !== produto)
      this.listInicial = novaLista
      this.carrinho.set(novaLista)


      console.log("this.listInicial", this.listInicial)
      console.log("this.carrinho", this.carrinho())
    }
  }


  precoTotal = computed(() => {
    return this.carrinho().reduce((acc, item) => acc + item.preco, 0);
  });


  alterQuantidade(item_id: string, novaQuantidade: number) {
    this.listInicial.filter(item => item._id === item_id).map(item => (item.quantidade = novaQuantidade));
    this.carrinho.set(this.listInicial)


    console.log("this.listInicial", this.listInicial)


  }

  getItensCarrinho() {
    return this.carrinho()
  }
  getTotalCarrinho() {
    return this.precoTotal()
  }

}
