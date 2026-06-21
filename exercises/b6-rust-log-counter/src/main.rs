use regex::Regex;
use std::collections::BTreeMap;
use std::env;
use std::fs;
use std::io::{self, BufRead};
use std::process;

pub fn count_levels(input: &str) -> BTreeMap<String, usize> {
    let re = Regex::new(r"\b(TRACE|DEBUG|INFO|WARN|ERROR|FATAL)\b").unwrap();
    let mut counts: BTreeMap<String, usize> = BTreeMap::new();
    for line in input.lines() {
        for cap in re.captures_iter(line) {
            let level = cap.get(1).unwrap().as_str().to_string();
            *counts.entry(level).or_default() += 1;
        }
    }
    counts
}

pub fn format_report(counts: &BTreeMap<String, usize>) -> String {
    let total: usize = counts.values().sum();
    let mut out = format!("total={total}\n");
    for (level, n) in counts {
        out.push_str(&format!("{level}={n}\n"));
    }
    out
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let input = if args.len() > 1 {
        fs::read_to_string(&args[1]).unwrap_or_else(|e| {
            eprintln!("read error: {e}");
            process::exit(1);
        })
    } else {
        let stdin = io::stdin();
        stdin
            .lock()
            .lines()
            .map_while(Result::ok)
            .collect::<Vec<_>>()
            .join("\n")
    };

    let counts = count_levels(&input);
    print!("{}", format_report(&counts));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn counts_mixed_levels() {
        let sample = "INFO boot\nWARN disk 90%\nERROR timeout\nINFO retry\nERROR crash";
        let counts = count_levels(sample);
        assert_eq!(counts.get("INFO"), Some(&2));
        assert_eq!(counts.get("WARN"), Some(&1));
        assert_eq!(counts.get("ERROR"), Some(&2));
    }

    #[test]
    fn empty_input_zero_total() {
        let counts = count_levels("");
        assert!(counts.is_empty());
    }
}
