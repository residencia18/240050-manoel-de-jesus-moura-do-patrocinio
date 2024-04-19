import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { type_suino } from '../../types/type_suino';
import { NgFor } from '@angular/common';
import { CardSuinoDetailComponent } from '../../components/card-suino-detail/card-suino-detail.component';
import { FilterSuinosComponent } from '../../components/filter-suinos/filter-suinos.component';

@Component({
  selector: 'app-listagem-suinos',
  standalone: true,
  imports: [NgFor,CardSuinoDetailComponent,FilterSuinosComponent],
  templateUrl: './listagem-suinos.component.html',
  styleUrl: './listagem-suinos.component.css'
})
export class ListagemSuinosComponent {
  listSuinos: type_suino[] = []
  filtedlistSuinos: type_suino[] = []
  optionSelected:any = { propriedade: null, valor: null };

  constructor(private apiService: ApiService){}

  ngOnInit(){
    this.apiService.getListaSuinos().subscribe((datas)=>{
      this.listSuinos=datas;
      this.filtedlistSuinos = this.listSuinos;
    })
  }

 

  filterList(filter: { propriedade: keyof type_suino, valor: string }) {
    this.filtedlistSuinos = this.listSuinos.filter(suino => suino[filter.propriedade] == filter.valor);

  }
  clearFilter(){
    this.filtedlistSuinos = this.listSuinos
  }
}
