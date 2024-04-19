import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { RegisterAtendComponent } from './pages/register-atend/register-atend.component';
import { ListAtendComponent } from './pages/list-atend/list-atend.component';

export const routes: Routes = [
    {path:"", component: HomeComponent},
    {path:"resgister-atend", component: RegisterAtendComponent},
    {path:"list-atend", component: ListAtendComponent}
];
