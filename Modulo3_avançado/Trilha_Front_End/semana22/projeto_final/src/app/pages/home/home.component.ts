import { Component } from '@angular/core';
import { CarouselComponent } from '../../components/carousel/carousel.component';
import { ApiService } from '../../services/api.service';
import { type_product } from '../../types/product';
import { catchError, throwError } from 'rxjs';
import Swal from 'sweetalert2';
import { NgFor, NgIf } from '@angular/common';
import { CardProductComponent } from '../../components/card-product/card-product.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CarouselComponent,NgIf,NgFor,CardProductComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  productlist: type_product[] = [];
  constructor(private apiService: ApiService) {}
  ngOnInit(){
    this.apiService.getAllProducts().pipe(
      catchError( error =>{
        console.error(error);
        Swal.fire({
          icon: 'error',
          title: 'Erro!',
          text: 'Ocorreu um erro ao buscar produtos. Por favor, tente novamente.'
        });
        return throwError(error);
      })
    )
    .subscribe((datas)=>{
      this.productlist = datas.slice(0,8)
      console.log("produtos",this.productlist)
    })
  }
}
