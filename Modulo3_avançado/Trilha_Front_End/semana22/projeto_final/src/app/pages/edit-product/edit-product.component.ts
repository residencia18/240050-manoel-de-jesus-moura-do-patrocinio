import { Component } from '@angular/core';
import { FormProductComponent } from '../../components/form-product/form-product.component';
import { type_product } from '../../types/product';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-edit-product',
  standalone: true,
  imports: [FormProductComponent],
  templateUrl: './edit-product.component.html',
  styleUrl: './edit-product.component.css'
})
export class EditProductComponent {
  produto: type_product|null
  produtoId: string

  
  constructor(public http: HttpClient,private rota: ActivatedRoute, private apiService: ApiService) {
    this.produto = null;
    this.produtoId = ""
  }
  ngOnInit(): void{
    this.produtoId = this.rota.snapshot.params['id']
    this.produtoId.length > 0 && this.apiService.getProductById(this.produtoId).subscribe((data)=>{
      this.produto = {...data, _id:this.produtoId} 
    })
    
  }
}
