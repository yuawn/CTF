package main

import(
  "net/http"
  "net/url"
  "log"
  "strings"
  "os"
)


func main(){
  log.Println(os.Args[1])
  log.Println(os.Args[2])
  form := url.Values{}
  form.Add("point", os.Args[1])
  form.Add("token", os.Args[2])
  req, _ := http.NewRequest("POST", "http://scoreboard:8001/submit", strings.NewReader(form.Encode()))
  req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
  resp, err := http.DefaultClient.Do(req)
  if err != nil {
    log.Println(err)
    return
  }
  defer resp.Body.Close()
}