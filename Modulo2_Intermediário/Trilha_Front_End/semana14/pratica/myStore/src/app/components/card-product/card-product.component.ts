import { Component, Input } from '@angular/core';
import { type_product } from '../../types/product';

@Component({
  selector: 'app-card-product',
  standalone: true,
  imports: [],
  templateUrl: './card-product.component.html',
  styleUrl: './card-product.component.css'
})
export class CardProductComponent {
  @Input() product: type_product| null = null;
}
