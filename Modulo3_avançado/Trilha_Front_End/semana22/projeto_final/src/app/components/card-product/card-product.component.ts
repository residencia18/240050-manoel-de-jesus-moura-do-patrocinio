import { Component, Input } from '@angular/core';
import { type_product } from '../../types/product';
// import { CarrinhoService } from '../../services/carrinho.service';
import Swal from 'sweetalert2';
import { RouterLink } from '@angular/router';
import { CarrinhoService } from '../../services/carrinho.service';

@Component({
  selector: 'app-card-product',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './card-product.component.html',
  styleUrl: './card-product.component.css'
})
export class CardProductComponent {
  @Input() product: type_product| null = null;

  constructor(private carrinhoService: CarrinhoService){}
 
  adicionarItem(item:type_product){

    this.carrinhoService.addItem(item)
    Swal.fire({
      icon: 'success',
      title: 'Adicionado !',
      timer:900,
      showConfirmButton: false,
    });
  }
}
