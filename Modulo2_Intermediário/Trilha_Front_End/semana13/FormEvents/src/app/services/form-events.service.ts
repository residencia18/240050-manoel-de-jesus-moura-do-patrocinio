import { Injectable } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FormEventsService {

  private fromEventsSubject = new Subject<string[]>();
  private fromDatasSubject = new Subject<any>();

  constructor() { }


  setFormEvent (formEventData:string[]){
    this.fromEventsSubject.next(formEventData);

  }
  getFormEvent (): Observable<string[]>{
    return this.fromEventsSubject.asObservable();
  }
  setFormData (formData:any){
    this.fromDatasSubject.next(formData);
   
  }
  getFormData (): Observable<any>{
    return this.fromDatasSubject.asObservable();
   
  }
  
}
