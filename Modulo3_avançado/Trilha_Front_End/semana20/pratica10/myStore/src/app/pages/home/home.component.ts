import { Component } from '@angular/core';
import { NavBarComponent } from '../../components/nav-bar/nav-bar.component';
import { BannerPromotionsComponent } from '../../components/banner-promotions/banner-promotions.component';
import { HttpClient } from '@angular/common/http';
import { ApiService } from '../../services/api.service';
import { catchError, throwError } from 'rxjs';
import Swal from 'sweetalert2';
import { type_product } from '../../types/product';
import { NgFor, NgIf } from '@angular/common';
import { CardProductComponent } from '../../components/card-product/card-product.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [NavBarComponent,BannerPromotionsComponent,NgFor,NgIf, CardProductComponent],
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
      this.productlist = datas.products.slice(0,8)
    })
  }

}
