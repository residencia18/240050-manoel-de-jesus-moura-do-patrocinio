import { Component, EventEmitter, Input, Output } from '@angular/core';
import { type_sessao } from '../../types/type_sessao';
import { ApiService } from '../../services/api.service';
import { NgIf } from '@angular/common';
import { FormatdatePipe } from '../../pipes/formatdate.pipe';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-card-manejo-detail',
  standalone: true,
  imports: [NgIf,FormatdatePipe,RouterLink],
  templateUrl: './card-manejo-detail.component.html',
  styleUrl: './card-manejo-detail.component.css'
})
export class CardManejoDetailComponent {
  @Input() sessao:type_sessao|null = null
  @Output() selectSessao  = new EventEmitter<type_sessao>();

  constructor(private apiService:ApiService){
  }
  deleteSuino(){
    console.log(this.sessao)
    // this.apiService.deleteSuinoById(this.suino!.id!)
  }
  emitterEvent(sessaoSelected:type_sessao) {
    // this.selectSuino.emit(suinoSelected)
  }

}
