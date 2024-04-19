import { Component, EventEmitter, Input, Output } from '@angular/core';
import { type_suino } from '../../types/type_suino';
import { NgIf } from '@angular/common';
import { RouterLink } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { DateInMonthsPipe } from '../../pipes/date-in-months.pipe';

@Component({
  selector: 'app-card-suino-detail',
  standalone: true,
  imports: [NgIf,RouterLink,DateInMonthsPipe],

  templateUrl: './card-suino-detail.component.html',
  styleUrl: './card-suino-detail.component.css'
})
export class CardSuinoDetailComponent {
  @Input() suino:type_suino|null = null
  @Input() CardType: ("normal" |"manejo")  = "normal"
  @Output() selectSuino  = new EventEmitter<type_suino>();

  constructor(private apiService:ApiService){
  }
  deleteSuino(){
    this.apiService.deleteSuinoById(this.suino!.id!)
  }
  emitterEvent(suinoSelected:type_suino) {
    this.selectSuino.emit(suinoSelected)
  }
}
