import { Component } from '@angular/core';
import { type_product } from '../../types/product';
import { ApiService } from '../../services/api.service';
import { catchError, throwError } from 'rxjs';
import Swal from 'sweetalert2';
import { NgFor, NgIf } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-painel-gerencia',
  standalone: true,
  imports: [NgIf,NgFor,RouterLink],
  templateUrl: './painel-gerencia.component.html',
  styleUrl: './painel-gerencia.component.css'
})
export class PainelGerenciaComponent {
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

  deleteProduct(product_id:string){
    this.apiService.apagarProdutoById(product_id)
  }
}
