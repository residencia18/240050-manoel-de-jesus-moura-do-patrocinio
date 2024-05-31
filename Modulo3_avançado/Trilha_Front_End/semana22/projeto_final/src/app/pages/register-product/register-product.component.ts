import { Component } from '@angular/core';
import { FormProductComponent } from '../../components/form-product/form-product.component';

@Component({
  selector: 'app-register-product',
  standalone: true,
  imports: [FormProductComponent],
  templateUrl: './register-product.component.html',
  styleUrl: './register-product.component.css'
})
export class RegisterProductComponent {

}
