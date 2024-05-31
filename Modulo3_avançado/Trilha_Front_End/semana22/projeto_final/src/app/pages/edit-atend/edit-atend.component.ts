import { Component } from '@angular/core';
import { FormAtendimentoComponent } from '../../components/form-atendimento/form-atendimento.component';
import { type_atendimento } from '../../types/atendimento';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-edit-atend',
  standalone: true,
  imports: [FormAtendimentoComponent],
  templateUrl: './edit-atend.component.html',
  styleUrl: './edit-atend.component.css'
})
export class EditAtendComponent {

  atendimento: type_atendimento|null
  atendimentoId: string

  
  constructor(public http: HttpClient,private rota: ActivatedRoute, private apiService: ApiService) {
    this.atendimento = null;
    this.atendimentoId = ""
  }
  ngOnInit(): void{
    this.atendimentoId = this.rota.snapshot.params['id']
    this.atendimentoId.length > 0 && this.apiService.getAtendimentoById(this.atendimentoId).subscribe((data)=>{
      this.atendimento = {...data, id:this.atendimentoId} 
    })
    
  }
}
