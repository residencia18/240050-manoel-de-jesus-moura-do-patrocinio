import { Component, Input, SimpleChanges } from '@angular/core';
import { type_atendimento } from '../../types/atendimento';
import { ApiService } from '../../services/api.service';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-atendimento-detail',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './atendimento-detail.component.html',
  styleUrl: './atendimento-detail.component.css'
})
export class AtendimentoDetailComponent {

  @Input() atendimento: type_atendimento | null = null;

  constructor(private apiService: ApiService) { }
  deleteAtend() {
    this.apiService.apagarAtendimentoById(this.atendimento?.id!)
  }


}
