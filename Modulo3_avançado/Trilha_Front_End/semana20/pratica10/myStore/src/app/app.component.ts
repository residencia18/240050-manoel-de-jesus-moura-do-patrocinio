import { Component, effect, Injector } from '@angular/core';
import { CommonModule, NgFor, NgIf } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { ApiService } from './services/api.service';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { AuthService } from './services/auth.service';
import { AuthInterceptor } from './interceptors/auth.interceptor';
import { CarrinhoService } from './services/carrinho.service';
import { type_product } from './types/product';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HttpClientModule, NavBarComponent, NgIf, NgFor],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService, AuthService, { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }]
})
export class AppComponent {
  title = 'myStore';
  carrinho: type_product[] = []
  totalCarrinho: number = 0
  public total: number = 0
  constructor(private authService: AuthService, private carrinhoService: CarrinhoService) { }


  ngOnInit() {
    this.authService.autoLogin();
    this.carrinho = this.carrinhoService.getItensCarrinho()
    this.totalCarrinho = this.carrinhoService.getTotalCarrinho()
  }

  updateTotalPrice() {
    this.ngOnInit()
    this.total = this.carrinhoService.carrinho().reduce((acc, item) => acc + (item.preco * item.quantidade!) , 0);

  }
  removeItem(item: type_product): void {
    this.carrinhoService.removeItem(item)
    Swal.fire({
      icon: 'success',
      title: 'Removido !',
      timer: 900,
      showConfirmButton: false,
    });
    this.ngOnInit()
    this.updateTotalPrice()
  }

  alterQuantidade(event:any, item_id:string){
    const quantidadeAtual = event.target.value;
    this.carrinhoService.alterQuantidade(item_id,quantidadeAtual)
    this.updateTotalPrice()
  }
}
