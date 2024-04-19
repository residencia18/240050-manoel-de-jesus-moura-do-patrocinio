import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { type_sessao } from '../../types/type_sessao';
import { CardManejoDetailComponent } from '../../components/card-manejo-detail/card-manejo-detail.component';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-list-manejo',
  standalone: true,
  imports: [CardManejoDetailComponent,NgFor],
  templateUrl: './list-manejo.component.html',
  styleUrl: './list-manejo.component.css'
})
export class ListManejoComponent {
  listOfsections: type_sessao[] = []
  constructor(private apiService: ApiService){}
  ngOnInit() {
    this.apiService.getListSessoes().subscribe((data)=>{
      console.log("DADOS RETORNADOS DA API",data)
      this.listOfsections = data
    })
  }
}
