import { Component } from '@angular/core';
import { AtendimentoDetailComponent } from '../../components/atendimento-detail/atendimento-detail.component';
import { ApiService } from '../../services/api.service';
import { type_atendimento } from '../../types/atendimento';
import { NgFor, NgIf } from '@angular/common';

@Component({
  selector: 'app-list-atend',
  standalone: true,
  imports: [AtendimentoDetailComponent, NgIf,NgFor],
  templateUrl: './list-atend.component.html',
  styleUrl: './list-atend.component.css'
})
export class ListAtendComponent {
  public atendimentos:type_atendimento[]|[] = [];
  constructor(private apiService: ApiService){}

  ngOnInit(){

      this.apiService.getAtendimento().subscribe((response)=>{
        console.log("response",response)
        this.atendimentos = response
      })

  }
}
