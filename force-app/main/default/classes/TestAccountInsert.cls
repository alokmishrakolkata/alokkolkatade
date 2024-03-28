@isTest //Annotation of test class Alok M
public class TestAccountInsert
{
//define testmethod 
 public static testmethod void testinsert()
 {
//Create new account instance and pass your name as string input 
  Account a = new Account(name = 'SalesforceKid');
//Append Mr. with the account name
  a.name = 'Mr.' + a.name;
  insert a;
  }
} 