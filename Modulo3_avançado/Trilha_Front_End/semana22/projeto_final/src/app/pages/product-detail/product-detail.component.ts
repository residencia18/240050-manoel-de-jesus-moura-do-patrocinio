import { Component } from '@angular/core';
import { type_product } from '../../types/product';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-product-detail',
  standalone: true,
  imports: [],
  templateUrl: './product-detail.component.html',
  styleUrl: './product-detail.component.css'
})
export class ProductDetailComponent {
  product: type_product|null
  product_id: string

  
  constructor(public http: HttpClient,private rota: ActivatedRoute, private apiService: ApiService) {
    this.product = null;
    this.product_id = ""
  }
  ngOnInit(): void{
    this.product_id = this.rota.snapshot.params['id']
    this.product_id.length > 0 && this.apiService.getProductById(this.product_id).subscribe((data)=>{
      this.product = {...data, _id:this.product_id} 
    })
    
  }
}
